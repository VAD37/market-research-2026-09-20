#!/usr/bin/env python3
"""infra/cf-tunnel.py -- Cloudflare Tunnel + DNS helper for the dev1/dev2/dev3 sites.

Python 3.9, stdlib only (urllib.request, json, os, argparse, re, base64, secrets).
No `requests` -- it is not installed on this machine.

Subcommands:
    verify   GET /user/tokens/verify -- proves the token in .env actually works.
    create   Create the named tunnel (idempotent) + the three dev1/2/3 CNAMEs.
    status   Show the tunnel and the three DNS records.
    destroy  Remove ONLY what `create` made (tracked in .cf-tunnel-state.json).

Safety rules enforced in code (not just documented):
  - ALLOWED_SUBDOMAINS is a hardcoded tuple. assert_subdomain_allowed() raises
    before any HTTP call is made for a name outside it.
  - create never overwrites or deletes a pre-existing DNS record. If dev1,
    dev2 or dev3 already resolves to something, it is reported and skipped.
  - destroy only ever acts on the tunnel id recorded in .cf-tunnel-state.json
    by a prior `create` run from this script, and only on the DNS record ids
    recorded there. It refuses if that state is missing or does not match
    the live tunnel's name. It never searches the account for tunnels by
    name pattern, so it structurally cannot touch `dev-vad`, `mcp` or
    `phongkham-bsXuan` -- those are pre-existing tunnels on this account
    that this script did not create.
  - create and destroy default to dry-run (no HTTP write calls -- reads used
    to check current state are still performed since they're needed to print
    an accurate plan). Pass --execute to actually do it. --dry-run is also
    accepted explicitly and always wins if both are given.
  - A token, account id, zone id or tunnel secret is never printed in full,
    anywhere, including dry-run output and error paths. mask() reduces each
    to its last 4 characters.
  - .env is parsed by hand: strip whitespace, strip trailing \\r (the file is
    CRLF), strip surrounding quotes. No third-party dotenv library.
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import re
import secrets
import sys
import urllib.error
import urllib.parse
import urllib.request

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

ALLOWED_SUBDOMAINS = ("dev1", "dev2", "dev3")
ZONE_APEX = "vad37.com"
API_BASE = "https://api.cloudflare.com/client/v4"

INFRA_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(INFRA_DIR)
ENV_PATH = os.path.join(REPO_ROOT, ".env")
STATE_PATH = os.path.join(INFRA_DIR, ".cf-tunnel-state.json")
DEFAULT_TUNNEL_NAME = "market-research-dev-sites"

# Tunnels already on this account that this script did NOT create. Never
# touched, never matched-by-name, listed here only so destroy's sanity check
# has something concrete to compare against.
KNOWN_FOREIGN_TUNNEL_NAMES = ("dev-vad", "mcp", "phongkham-bsXuan")

UUID_RE = re.compile(
    r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"
)
HEX32_RE = re.compile(r"^[0-9a-fA-F]{32}$")


class SubdomainNotAllowed(ValueError):
    pass


# ---------------------------------------------------------------------------
# Small helpers
# ---------------------------------------------------------------------------


def mask(value):
    """Mask a secret to its last 4 characters. Never print the raw value."""
    if not value:
        return "<empty>"
    if len(value) <= 4:
        return "*" * len(value)
    return "*" * (len(value) - 4) + value[-4:]


def assert_subdomain_allowed(name):
    """Raise SubdomainNotAllowed for any name outside ALLOWED_SUBDOMAINS.

    Called before any HTTP call that would write a DNS record for `name`.
    """
    if name not in ALLOWED_SUBDOMAINS:
        raise SubdomainNotAllowed(
            "refusing to touch DNS for '{}': not in the hardcoded allowlist {}. "
            "No HTTP call was made.".format(name, ALLOWED_SUBDOMAINS)
        )
    return True


def parse_env(path):
    """Tiny .env parser: strip whitespace, strip CR, strip surrounding quotes."""
    values = {}
    if not os.path.isfile(path):
        return values
    with open(path, "r", encoding="utf-8") as f:
        for raw_line in f:
            line = raw_line.strip("\r\n").strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, val = line.partition("=")
            key = key.strip()
            val = val.strip()
            if len(val) >= 2 and val[0] == val[-1] and val[0] in ("'", '"'):
                val = val[1:-1]
            values[key] = val
    return values


def load_credentials():
    env = parse_env(ENV_PATH)
    return (
        env.get("CLOUDFLARE_ACCOUNT_ID", ""),
        env.get("CLOUDFLARE_API_TOKEN", ""),
        env.get("CLOUDFLARE_ZONE_ID", ""),
    )


def shape_diagnosis(name, value):
    """Return a human diagnosis string if `value` looks like the wrong shape
    for a Cloudflare id/token, else None.

    This intentionally does NOT hard-fail on "unexpected" token shapes --
    Cloudflare has shipped more than one valid token format (e.g. a `cfut_`
    prefixed value around 53 chars, seen 2026-09-17), so only a positive
    match against a KNOWN-wrong shape (a canonical UUID) is flagged as an
    error. Anything else just gets a softer note for account/zone ids, and
    no note at all for the token, whose valid shapes are not stable enough
    to gate on.
    """
    if not value:
        return "{} is empty in .env.".format(name)
    if UUID_RE.match(value):
        return (
            "{} looks like a canonical UUID (36 chars, 8-4-4-4-12, with hyphens). "
            "Cloudflare account/zone IDs are 32 lowercase-hex characters with no "
            "hyphens, and API tokens do not contain hyphens either. This is very "
            "likely the wrong value pasted into .env.".format(name)
        )
    if name in ("CLOUDFLARE_ACCOUNT_ID", "CLOUDFLARE_ZONE_ID") and not HEX32_RE.match(value):
        return (
            "{} is {} characters and is not 32 lowercase-hex characters. It may "
            "still be a valid Cloudflare id if the format has changed, but it does "
            "not match the historical shape.".format(name, len(value))
        )
    return None


def cf_api(method, path, token, body=None, params=None):
    """Minimal urllib wrapper. Returns (http_status, parsed_json_or_dict)."""
    url = API_BASE + path
    if params:
        query = "&".join("{}={}".format(k, urllib.parse.quote(str(v))) for k, v in params.items())
        url = "{}?{}".format(url, query)
    data = json.dumps(body).encode("utf-8") if body is not None else None
    headers = {
        "Authorization": "Bearer {}".format(token),
        "Content-Type": "application/json",
        "User-Agent": "cf-tunnel.py/1.0",
    }
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            raw = resp.read().decode("utf-8")
            return resp.getcode(), (json.loads(raw) if raw else {})
    except urllib.error.HTTPError as e:
        raw = e.read().decode("utf-8")
        try:
            parsed = json.loads(raw) if raw else {}
        except ValueError:
            parsed = {"success": False, "errors": [{"message": "<non-JSON response body>"}]}
        return e.code, parsed
    except urllib.error.URLError as e:
        return 0, {"success": False, "errors": [{"message": "connection error: {}".format(e.reason)}]}


def has_error_code(resp_json, code):
    for err in (resp_json or {}).get("errors", []) or []:
        if err.get("code") == code:
            return True
    return False


def load_state():
    if not os.path.isfile(STATE_PATH):
        return {}
    with open(STATE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_state(state):
    with open(STATE_PATH, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)
    try:
        os.chmod(STATE_PATH, 0o600)
    except OSError:
        pass  # best-effort on platforms/filesystems that ignore POSIX modes


# ---------------------------------------------------------------------------
# verify
# ---------------------------------------------------------------------------


def cmd_verify(args):
    account_id, token, zone_id = load_credentials()

    print("Reading credentials from: {}".format(ENV_PATH))
    ok_shape = True
    for name, value in (
        ("CLOUDFLARE_ACCOUNT_ID", account_id),
        ("CLOUDFLARE_API_TOKEN", token),
        ("CLOUDFLARE_ZONE_ID", zone_id),
    ):
        diag = shape_diagnosis(name, value)
        if diag:
            ok_shape = False
            print("  [{}] {} = {} -- {}".format("SHAPE-WARN", name, mask(value), diag))
        else:
            print("  [ok] {} = {} ({} chars)".format(name, mask(value), len(value)))

    if not token:
        print("\nNo CLOUDFLARE_API_TOKEN found in .env -- cannot call the API.")
        return 1

    print("\nGET /user/tokens/verify")
    status, resp = cf_api("GET", "/user/tokens/verify", token)
    success = bool(resp.get("success"))
    print("HTTP {}".format(status))
    print(json.dumps(resp, indent=2))

    if success:
        print("\nToken is valid.")
        if not ok_shape:
            print(
                "Note: the shape warnings above did not stop this call, but they "
                "flagged a value worth double-checking."
            )
        return 0

    print("\nToken verification FAILED.")
    if not ok_shape:
        print("Likely cause -- credential shape:")
        for name, value in (
            ("CLOUDFLARE_ACCOUNT_ID", account_id),
            ("CLOUDFLARE_API_TOKEN", token),
            ("CLOUDFLARE_ZONE_ID", zone_id),
        ):
            diag = shape_diagnosis(name, value)
            if diag:
                print("  - {}: {}".format(name, diag))
    else:
        print(
            "Shapes look plausible, so this is likely a revoked/expired token, a "
            "typo, or a token scoped to the wrong account -- not a formatting issue."
        )
    return 1


# ---------------------------------------------------------------------------
# create
# ---------------------------------------------------------------------------


def find_dns_record(zone_id, token, fqdn):
    """Return (status, record_or_none, error_resp_or_none)."""
    status, resp = cf_api(
        "GET", "/zones/{}/dns_records".format(zone_id), token, params={"name": fqdn}
    )
    if status != 200 or not resp.get("success"):
        return status, None, resp
    results = resp.get("result") or []
    return status, (results[0] if results else None), None


def cmd_create(args):
    account_id, token, zone_id = load_credentials()
    dry_run = not args.execute or args.dry_run  # --dry-run always wins
    name = args.name or DEFAULT_TUNNEL_NAME

    print("mode: {}".format("DRY RUN (no writes)" if dry_run else "EXECUTE"))
    print("account: {}  zone: {}  tunnel name: {}".format(mask(account_id), mask(zone_id), name))

    if not (account_id and token and zone_id):
        print("Missing one or more of CLOUDFLARE_ACCOUNT_ID / _API_TOKEN / _ZONE_ID in .env.")
        return 1

    state = load_state()
    tunnel_id = state.get("tunnel_id")
    tunnel_secret_b64 = None

    # --- tunnel half -------------------------------------------------
    if tunnel_id:
        print("\nExisting tunnel recorded in state: id ends '...{}' name '{}' -- reusing, not recreating.".format(
            tunnel_id[-4:], state.get("tunnel_name")
        ))
    else:
        print("\nAccount -> Cloudflare Tunnel -> Edit call:")
        print("  POST /accounts/{}/cfd_tunnel  body: {{name: {!r}, config_src: local, tunnel_secret: <32 random bytes, not shown>}}".format(
            mask(account_id), name
        ))
        if dry_run:
            print("  (dry run -- not sent)")
        else:
            tunnel_secret_b64 = base64.b64encode(secrets.token_bytes(32)).decode("ascii")
            status, resp = cf_api(
                "POST",
                "/accounts/{}/cfd_tunnel".format(account_id),
                token,
                body={"name": name, "config_src": "local", "tunnel_secret": tunnel_secret_b64},
            )
            if status not in (200, 201) or not resp.get("success"):
                print("  FAILED: HTTP {} -- {}".format(status, _safe_errors(resp)))
                return 1
            tunnel_id = resp["result"]["id"]
            print("  created tunnel id ...{}".format(tunnel_id[-4:]))

            creds_path = os.path.join(INFRA_DIR, "{}-credentials.json".format(tunnel_id))
            with open(creds_path, "w", encoding="utf-8") as f:
                json.dump(
                    {
                        "AccountTag": account_id,
                        "TunnelSecret": tunnel_secret_b64,
                        "TunnelID": tunnel_id,
                        "TunnelName": name,
                    },
                    f,
                )
            try:
                os.chmod(creds_path, 0o600)
            except OSError:
                pass
            print("  credentials written to: {} (never printed)".format(creds_path))

            state.update({"tunnel_id": tunnel_id, "tunnel_name": name, "dns_records": state.get("dns_records", {})})
            save_state(state)

    # --- DNS half ------------------------------------------------------
    dns_records = state.get("dns_records", {})
    permission_blocked = False

    for sub in ALLOWED_SUBDOMAINS:
        assert_subdomain_allowed(sub)  # raises before any HTTP call if this ever drifts
        fqdn = "{}.{}".format(sub, ZONE_APEX)

        print("\nZone -> DNS -> Edit check for {}:".format(fqdn))
        print("  GET /zones/{}/dns_records?name={}".format(mask(zone_id), fqdn))

        if dry_run:
            print("  (dry run -- not sent)")
            continue

        status, existing, err = find_dns_record(zone_id, token, fqdn)
        if err is not None:
            if has_error_code(err, 10000):
                permission_blocked = True
                print(
                    "  BLOCKED: HTTP {} code 10000 (Authentication error). The API token is "
                    "missing 'Zone -> DNS -> Edit' on zone {} (fqdn {}). Add that permission to "
                    "the token, scoped to vad37.com, then re-run `create` -- the tunnel "
                    "(id ...{}) already exists and will not be recreated.".format(
                        status, mask(zone_id), fqdn, tunnel_id[-4:] if tunnel_id else "????"
                    )
                )
                continue
            print("  FAILED: HTTP {} -- {}".format(status, _safe_errors(err)))
            continue

        if existing is not None:
            print(
                "  EXISTS: {} record already present (id ends '...{}', content '{}'). "
                "Not touching it.".format(existing.get("type"), existing.get("id", "")[-4:], existing.get("content"))
            )
            continue

        target = "{}.cfargotunnel.com".format(tunnel_id)
        print("  POST /zones/{}/dns_records  body: {{type: CNAME, name: {}, content: {}, proxied: true}}".format(
            mask(zone_id), fqdn, target
        ))
        status, resp = cf_api(
            "POST",
            "/zones/{}/dns_records".format(zone_id),
            token,
            body={"type": "CNAME", "name": fqdn, "content": target, "proxied": True},
        )
        if status not in (200, 201) or not resp.get("success"):
            if has_error_code(resp, 10000):
                permission_blocked = True
                print(
                    "  BLOCKED: HTTP {} code 10000 (Authentication error) -- missing "
                    "'Zone -> DNS -> Edit' on zone {}.".format(status, mask(zone_id))
                )
            else:
                print("  FAILED: HTTP {} -- {}".format(status, _safe_errors(resp)))
            continue

        record_id = resp["result"]["id"]
        dns_records[sub] = {"record_id": record_id, "fqdn": fqdn}
        print("  created CNAME {} -> {} (record id ...{})".format(fqdn, target, record_id[-4:]))

    if not dry_run:
        state["dns_records"] = dns_records
        save_state(state)

    if dry_run:
        print("\nDry run complete. Re-run with --execute to actually create the tunnel and records.")
        return 0

    if permission_blocked:
        print(
            "\nPartial success: tunnel half OK, DNS half blocked by missing token permission. "
            "See messages above for exactly what to add."
        )
        return 2

    print("\ncreate complete.")
    return 0


def _safe_errors(resp):
    """Format API error list without ever leaking a secret that might be
    echoed back inside an error message (defensive; Cloudflare error bodies
    do not normally contain the token, but we don't trust that blindly)."""
    errors = (resp or {}).get("errors") or []
    return "; ".join("{}: {}".format(e.get("code"), e.get("message")) for e in errors) or "<no error detail>"


# ---------------------------------------------------------------------------
# status
# ---------------------------------------------------------------------------


def cmd_status(args):
    account_id, token, zone_id = load_credentials()
    state = load_state()
    tunnel_id = state.get("tunnel_id")

    print("state file: {}".format(STATE_PATH if os.path.isfile(STATE_PATH) else "<none>"))

    if tunnel_id:
        status, resp = cf_api(
            "GET", "/accounts/{}/cfd_tunnel/{}".format(account_id, tunnel_id), token
        )
        if status == 200 and resp.get("success"):
            t = resp["result"]
            print(
                "tunnel: name={} id=...{} status={} connections={}".format(
                    t.get("name"), tunnel_id[-4:], t.get("status"), len(t.get("connections") or [])
                )
            )
        else:
            print("tunnel: recorded id ...{} but lookup failed: HTTP {} -- {}".format(
                tunnel_id[-4:], status, _safe_errors(resp)
            ))
    else:
        print("tunnel: none created by this script yet (no state file / no tunnel_id).")

    print()
    for sub in ALLOWED_SUBDOMAINS:
        fqdn = "{}.{}".format(sub, ZONE_APEX)
        status, existing, err = find_dns_record(zone_id, token, fqdn)
        if err is not None:
            if has_error_code(err, 10000):
                print("{}: DNS lookup BLOCKED -- token missing Zone -> DNS -> Edit on {}".format(fqdn, mask(zone_id)))
            else:
                print("{}: DNS lookup failed -- HTTP {} {}".format(fqdn, status, _safe_errors(err)))
            continue
        if existing is None:
            print("{}: no DNS record".format(fqdn))
        else:
            print("{}: {} -> {} (id ...{})".format(fqdn, existing.get("type"), existing.get("content"), existing.get("id", "")[-4:]))
    return 0


# ---------------------------------------------------------------------------
# destroy
# ---------------------------------------------------------------------------


def cmd_destroy(args):
    account_id, token, zone_id = load_credentials()
    dry_run = not args.execute or args.dry_run
    state = load_state()
    tunnel_id = state.get("tunnel_id")
    tunnel_name = state.get("tunnel_name")

    print("mode: {}".format("DRY RUN (no writes)" if dry_run else "EXECUTE"))

    if not tunnel_id:
        print(
            "Nothing to destroy: no tunnel_id recorded in {}. This command only ever acts on "
            "what its own `create` run recorded -- it will not search the account for tunnels "
            "by name.".format(STATE_PATH)
        )
        return 0

    if tunnel_name in KNOWN_FOREIGN_TUNNEL_NAMES:
        # Should never happen since we never write a foreign name into our own
        # state, but this is the hardcoded refusal the brief asked for.
        print(
            "REFUSING: state file names '{}', which is a known pre-existing tunnel this "
            "script did not create. Not touching it.".format(tunnel_name)
        )
        return 1

    print("recorded tunnel: name={} id=...{}".format(tunnel_name, tunnel_id[-4:]))

    if not dry_run:
        # Defense in depth: confirm the live tunnel's name still matches what
        # we recorded before deleting anything.
        status, resp = cf_api("GET", "/accounts/{}/cfd_tunnel/{}".format(account_id, tunnel_id), token)
        if status != 200 or not resp.get("success"):
            print("REFUSING: could not confirm live tunnel identity before destroy: HTTP {} -- {}".format(
                status, _safe_errors(resp)
            ))
            return 1
        live_name = resp["result"].get("name")
        if live_name != tunnel_name:
            print(
                "REFUSING: live tunnel name '{}' does not match recorded name '{}'. "
                "Not touching it.".format(live_name, tunnel_name)
            )
            return 1

    dns_records = state.get("dns_records", {})
    for sub, info in list(dns_records.items()):
        assert_subdomain_allowed(sub)
        record_id = info["record_id"]
        print("\nDELETE /zones/{}/dns_records/...{}  ({})".format(mask(zone_id), record_id[-4:], info["fqdn"]))
        if dry_run:
            print("  (dry run -- not sent)")
            continue
        status, resp = cf_api("DELETE", "/zones/{}/dns_records/{}".format(zone_id, record_id), token)
        if status == 200 and resp.get("success"):
            print("  deleted.")
            del dns_records[sub]
        else:
            print("  FAILED: HTTP {} -- {}".format(status, _safe_errors(resp)))

    print("\nDELETE /accounts/{}/cfd_tunnel/...{}".format(mask(account_id), tunnel_id[-4:]))
    if dry_run:
        print("  (dry run -- not sent)")
        print("\nDry run complete. Re-run with --execute to actually delete these.")
        return 0

    status, resp = cf_api("DELETE", "/accounts/{}/cfd_tunnel/{}".format(account_id, tunnel_id), token)
    if status == 200 and resp.get("success"):
        print("  deleted.")
        creds_path = os.path.join(INFRA_DIR, "{}-credentials.json".format(tunnel_id))
        if os.path.isfile(creds_path):
            os.remove(creds_path)
            print("  removed {}".format(creds_path))
        if os.path.isfile(STATE_PATH):
            os.remove(STATE_PATH)
            print("  removed {}".format(STATE_PATH))
        return 0

    print("  FAILED: HTTP {} -- {}".format(status, _safe_errors(resp)))
    state["dns_records"] = dns_records
    save_state(state)
    return 1


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------


def build_parser():
    p = argparse.ArgumentParser(description="Cloudflare Tunnel + DNS helper for dev1/dev2/dev3.")
    sub = p.add_subparsers(dest="command", required=True)

    sub.add_parser("verify", help="Check the .env credentials against the live API.")

    p_create = sub.add_parser("create", help="Create the tunnel and the three DNS records (idempotent).")
    p_create.add_argument("--name", default=None, help="Tunnel name (default: {})".format(DEFAULT_TUNNEL_NAME))
    p_create.add_argument("--execute", action="store_true", help="Actually make the API calls.")
    p_create.add_argument("--dry-run", action="store_true", help="Force dry run even if --execute is given.")

    sub.add_parser("status", help="Show the tunnel and the three DNS records.")

    p_destroy = sub.add_parser("destroy", help="Remove only what `create` made.")
    p_destroy.add_argument("--execute", action="store_true", help="Actually make the API calls.")
    p_destroy.add_argument("--dry-run", action="store_true", help="Force dry run even if --execute is given.")

    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    handlers = {
        "verify": cmd_verify,
        "create": cmd_create,
        "status": cmd_status,
        "destroy": cmd_destroy,
    }
    return handlers[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
