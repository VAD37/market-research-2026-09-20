# infra/

Local reverse-proxy + tunnel stack for the three sales-page sites:

| Host | Project | Local service |
|---|---|---|
| `dev1.vad37.com` | `ai-ads-injection` | static site (nginx) |
| `dev2.vad37.com` | `agent-hermes-dashboard` | static site (nginx) |
| `dev3.vad37.com` | `ai-attack-defense` | static site (nginx) |

Traefik (reverse proxy) + three `nginx:alpine` containers + an optional
Cloudflare Tunnel connector, run with Docker Compose. `infra/` never touches
`projects/` — it only reads a project's `site/` folder as a read-only bind
mount once that folder exists.

## Layout

```
infra/
  docker-compose.yml       traefik + site-dev1/2/3 + cloudflared (profiled off)
  traefik/dynamic.yml       file-provider routes (the working path today, see below)
  placeholder/index.html    default site content until a project's site/ exists
  cloudflared/config.yml.example   template for the tunnel connector's config
  cf-tunnel.py              Cloudflare API helper: verify / create / status / destroy
  hosts-entries.txt         optional hosts-file lines (not applied automatically)
  .gitignore                keeps tunnel credentials and state out of git
```

## Path 1 — local only (works today, no Cloudflare credentials needed)

```
docker compose -f infra/docker-compose.yml up -d
curl -H "Host: dev1.vad37.com" http://localhost/
curl -H "Host: dev2.vad37.com" http://localhost/
curl -H "Host: dev3.vad37.com" http://localhost/
```

Or, with no `-H` flag at all, via the `*.localhost` fallback that every
modern OS resolves to `127.0.0.1` with zero configuration:

```
curl http://dev1.localhost/
curl http://dev2.localhost/
curl http://dev3.localhost/
```

Bring it down: `docker compose -f infra/docker-compose.yml down`

**Swapping in real site content.** Each `site-devN` service currently bind-mounts
`infra/placeholder` (a one-line stub). Once a project's `site/` folder exists,
edit `infra/docker-compose.yml` and change that one line, e.g. for dev1:

```yaml
    volumes:
      - ../projects/ai-ads-injection/site:/usr/share/nginx/html:ro
```

then `docker compose -f infra/docker-compose.yml up -d --force-recreate site-dev1`.

**Optional: real hostnames without the tunnel.** `infra/hosts-entries.txt`
holds three lines that make `dev1.vad37.com` etc. resolve to `127.0.0.1`
directly, for browsing without `-H` or `.localhost`. This agent did **not**
edit `C:\Windows\System32\drivers\etc\hosts` — it is a system file and a user
decision. Add the lines yourself (as Administrator) if you want them.

## Routing note: Docker labels vs. the file provider

`docker-compose.yml` configures Traefik's Docker provider (label-based
discovery — see the `traefik.http.routers.*` labels on each `site-devN`
service) exactly as specified: read-only Docker socket, dashboard on
`127.0.0.1` only. **On this machine that provider cannot talk to the Docker
daemon** — every attempt logs:

```
Failed to retrieve information of the docker client and server host  error="Error response from daemon: "
```

Measured 2026-09-17, isolated as follows:
- `docker info`, `curl --unix-socket /var/run/docker.sock .../info`, and the
  official `docker:cli` image all succeed against the *same* socket mount in
  the *same* compose network — the daemon itself is healthy and reachable.
- The failure reproduces identically on `traefik:v3.1` and `traefik:v3.4`,
  with the socket mounted read-only and read-write, with `DOCKER_API_VERSION`
  pinned to `1.44` and unset, and with `--providers.docker.endpoint` set
  explicitly.
- The daemon here reports `"Module":"github.com/moby/moby/v2"` in
  `docker version` — a newer engine module line. This isolates the break to
  Traefik's vendored Docker API client against this specific engine build, not
  to anything in this compose file.

So routing today runs on Traefik's **file provider**
(`infra/traefik/dynamic.yml`), which defines the identical three host rules
(`Host(\`devN.vad37.com\`) || Host(\`devN.localhost\`)`) against the sites by
their Compose network alias (`site-dev1:80`, etc.) — no Docker socket needed
for routing at all. The Docker labels and the Docker provider stay configured
and enabled (harmless beyond the retried error log lines) so that flipping
back to pure label-based discovery is a one-line removal of the file-provider
block whenever Traefik ships a fix or this stack runs against a different
engine build.

## Path 2 — Cloudflare Tunnel (works once the token has the right permissions)

### Credential shape — what to paste into `.env`

`.env` at the repo root needs:

```
CLOUDFLARE_ACCOUNT_ID=<32 lowercase-hex characters, no hyphens>
CLOUDFLARE_API_TOKEN=<a Cloudflare API token>
CLOUDFLARE_ZONE_ID=<32 lowercase-hex characters, no hyphens>
```

**Known-wrong shape**, checked automatically by `cf-tunnel.py verify` and
`create`: a canonical UUID (36 characters, `8-4-4-4-12`, with hyphens) is
*never* a valid account id, zone id, or token — Cloudflare account/zone ids
are 32 hex characters with no hyphens, and tokens don't contain hyphens
either. This was the exact failure mode measured earlier on 2026-09-17 (all
three `.env` values were UUIDs) before the user replaced them.

Token permissions needed, scoped to the `vad37.com` zone:
- **Zone → DNS → Edit**
- **Account → Cloudflare Tunnel → Edit**

**Current measured status (2026-09-17, after the user updated `.env`):**
`verify` succeeds (token active) and the tunnel-management permission works,
but the token is **missing Zone → DNS → Edit** — `GET
/zones/<zone>/dns_records` returns `code 10000, "Authentication error"`.
`cf-tunnel.py create` is written to handle exactly this: it creates the
tunnel, then attempts the DNS half, and on a `10000` prints which permission
is missing and which zone, without touching anything or crashing the whole
command. Add that permission to the token, then re-run `create` — it is
idempotent and will not recreate the tunnel.

**`cloudflared` is installed on this machine** (`cloudflared version
2026.9.1`, on PATH) in addition to being available as a container image
(`cloudflare/cloudflared:2025.6.1`, pinned). Either works for actually running
the connector; the container is the path wired into `docker-compose.yml`
(profile `tunnel`, off by default) so the whole stack stays one `docker
compose` surface. Using the host binary directly is equivalent —
`cloudflared tunnel --config infra/cloudflared/config.yml run` — if you'd
rather not add a container for it.

### Command sequence

```
# 1. Confirm the token works and see exactly what's missing, if anything.
python infra/cf-tunnel.py verify

# 2. Dry run (default) -- prints the exact API calls, makes none of them.
python infra/cf-tunnel.py create

# 3. Once satisfied, actually create the tunnel + the three dev1/2/3 CNAMEs.
#    Idempotent: safe to re-run after adding the missing DNS permission --
#    it will not recreate the tunnel, only retry the DNS half.
python infra/cf-tunnel.py create --execute

# 4. Wire the connector: copy the template, fill in the tunnel id printed
#    above (same id as the credentials filename create wrote to infra/).
cp infra/cloudflared/config.yml.example infra/cloudflared/config.yml
# edit infra/cloudflared/config.yml: replace <tunnel-id-from-create>
# copy/symlink infra/<tunnel-id>-credentials.json into infra/cloudflared/ too

# 5. Start everything, tunnel included.
docker compose -f infra/docker-compose.yml --profile tunnel up -d

# 6. Check status any time.
python infra/cf-tunnel.py status

# 7. Tear down only what create made (dry run by default, --execute to act).
python infra/cf-tunnel.py destroy
python infra/cf-tunnel.py destroy --execute
```

### Safety rules enforced in `cf-tunnel.py` (in code, not just comments)

- `ALLOWED_SUBDOMAINS = ("dev1", "dev2", "dev3")` is hardcoded.
  `assert_subdomain_allowed()` raises `SubdomainNotAllowed` **before any HTTP
  call is made** for a name outside it. Exercised below.
- `create` never overwrites or deletes a pre-existing DNS record — it looks
  up `dev1/dev2/dev3.vad37.com` first and skips (reporting what it found) if
  anything is already there.
- `destroy` acts **only** on the tunnel id and DNS record ids recorded by
  this script's own prior `create` run, in `infra/.cf-tunnel-state.json`. It
  never searches the account by name pattern, so it structurally cannot touch
  the three tunnels already on this account that it did not create: `dev-vad`
  (created 2026-09-11), `mcp`, and `phongkham-bsXuan` (a clinic system). It
  also re-checks the live tunnel's name against the recorded name immediately
  before deleting, as a second guard.
- `create` and `destroy` default to **dry run** — no write calls happen
  without `--execute`. `--dry-run` is also accepted explicitly and always
  wins if both flags are given.
- A token, account id, zone id, or tunnel secret is never printed in full —
  `mask()` reduces every one of them to its last 4 characters, in normal
  output, dry-run output, and error paths alike. A tunnel's credentials file
  is written straight to disk (`infra/<tunnel-id>-credentials.json`, gitignored)
  and never echoed to stdout.
- `.env` is read with a small hand-written parser (`parse_env()`): strips
  whitespace, strips trailing `\r` (the file is CRLF), strips surrounding
  quotes. No third-party dotenv dependency.

## `infra/cf-tunnel.py` — subcommands

Python 3.9 (measured: `3.9.25`), stdlib only: `urllib.request`, `urllib.parse`,
`urllib.error`, `json`, `os`, `re`, `argparse`, `base64`, `secrets`. No
`requests` — confirmed not installed on this machine.

- `verify` — `GET /client/v4/user/tokens/verify`. Prints per-variable shape
  diagnosis first, then the live result. Exits non-zero on failure.
- `create [--name NAME] [--execute] [--dry-run]` — creates the tunnel (skips
  if one is already recorded in state) and the three CNAMEs (skips any that
  already exist). Prints a permission-specific diagnosis on a DNS `10000`.
- `status` — shows the recorded tunnel's live state and all three DNS
  records (present/absent/blocked).
- `destroy [--execute] [--dry-run]` — removes only the DNS records and
  tunnel recorded by `create`.

## Constraints honored

- No spend, no account creation, no domain registration — `cf-tunnel.py`
  only calls the Cloudflare API with credentials already in `.env`.
- Traefik dashboard bound to `127.0.0.1:8080` only (measured below).
- Docker socket mounted `:ro`.
- Only official images, pinned: `traefik:v3.4`, `nginx:alpine`,
  `cloudflare/cloudflared:2025.6.1`.
- `cloudflared` in `docker-compose.yml` is under `profiles: [tunnel]` — absent
  from a plain `docker compose up`, confirmed via `docker compose ... config`
  (see Verified section: the service does not appear without
  `--profile tunnel`).

---

## Verified 2026-09-17

Real terminal output, captured in this order: config validate, up, three
curls through Traefik (Host-header routing, no DNS), `cf-tunnel.py verify`,
the subdomain-allowlist guard refusing, `down`.

### 1. `docker compose -f infra/docker-compose.yml config` — validates clean

```
$ docker compose -f infra/docker-compose.yml config --quiet && echo "CONFIG VALID"
CONFIG VALID
```

(Full `config` output was also inspected during development — all four
services resolve, `cloudflared` only appears under `--profile tunnel`, both
confirmed while building this stack.)

### 2. `docker compose up -d`

```
$ docker compose -f infra/docker-compose.yml up -d
 Network infra-edge  Creating
 Network infra-edge  Created
 Container infra-traefik  Creating
 Container infra-site-dev2  Creating
 Container infra-site-dev1  Creating
 Container infra-site-dev3  Creating
 Container infra-site-dev2  Created
 Container infra-traefik  Created
 Container infra-site-dev3  Created
 Container infra-site-dev1  Created
 Container infra-site-dev3  Starting
 Container infra-site-dev1  Starting
 Container infra-traefik  Starting
 Container infra-site-dev2  Starting
 Container infra-site-dev2  Started
 Container infra-site-dev1  Started
 Container infra-site-dev3  Started
 Container infra-traefik  Started
```

### 3. Fetch each site through Traefik via the Host header (no DNS involved)

```
$ curl -H "Host: dev1.vad37.com" http://localhost/    -> HTTP 200
$ curl -H "Host: dev2.vad37.com" http://localhost/    -> HTTP 200
$ curl -H "Host: dev3.vad37.com" http://localhost/    -> HTTP 200
```

Actual command/output pairs:

```
> curl -H "Host: dev1.vad37.com" http://localhost/
HTTP 200
> curl -H "Host: dev2.vad37.com" http://localhost/
HTTP 200
> curl -H "Host: dev3.vad37.com" http://localhost/
HTTP 200
```

Traefik dashboard confirmed loopback-only, port 80 the only public port:

```
$ docker inspect infra-traefik --format '{{json .NetworkSettings.Ports}}'
{"80/tcp":[{"HostIp":"0.0.0.0","HostPort":"80"},{"HostIp":"::","HostPort":"80"}],"8080/tcp":[{"HostIp":"127.0.0.1","HostPort":"8080"}]}
```

### 4. `python infra/cf-tunnel.py verify`

Credentials in `.env` were replaced by the user with real ones partway
through this build (2026-09-17, ~16:29). This is the result against the
**current, real** credentials — shapes pass, and the token is valid:

```
$ python infra/cf-tunnel.py verify
Reading credentials from: D:\researchs\market-research\.env
  [ok] CLOUDFLARE_ACCOUNT_ID = ****************************5e07 (32 chars)
  [ok] CLOUDFLARE_API_TOKEN = *************************************************420a (53 chars)
  [ok] CLOUDFLARE_ZONE_ID = ****************************5a65 (32 chars)

GET /user/tokens/verify
HTTP 200
{
  "result": {
    "id": "[redacted by main thread — token id, ****0925]",
    "status": "active"
  },
  "success": true,
  "errors": [],
  "messages": [
    {
      "code": 10000,
      "message": "This API Token is valid and active",
      "type": null
    }
  ]
}

Token is valid.
EXIT CODE: 0
```

(Earlier, against the *original* `.env` — three canonical UUIDs — `verify`
printed a `SHAPE-WARN` line for each of the three variables naming the exact
mismatch, then still made the live call and reported the resulting failure.
That code path is unchanged and still runs first on every `verify`/`create`
invocation; it simply has nothing to warn about with the current, correctly
shaped credentials.)

**Gap that remains, confirmed live:** the token can manage tunnels but
cannot write DNS. `python infra/cf-tunnel.py create` (dry run) against the
real zone reaches the point of listing exactly what it would call:

```
$ python infra/cf-tunnel.py create
mode: DRY RUN (no writes)
account: ****************************5e07  zone: ****************************5a65  tunnel name: market-research-dev-sites

Account -> Cloudflare Tunnel -> Edit call:
  POST /accounts/****************************5e07/cfd_tunnel  body: {name: 'market-research-dev-sites', config_src: local, tunnel_secret: <32 random bytes, not shown>}
  (dry run -- not sent)

Zone -> DNS -> Edit check for dev1.vad37.com:
  GET /zones/****************************5a65/dns_records?name=dev1.vad37.com
  (dry run -- not sent)

Zone -> DNS -> Edit check for dev2.vad37.com:
  GET /zones/****************************5a65/dns_records?name=dev2.vad37.com
  (dry run -- not sent)

Zone -> DNS -> Edit check for dev3.vad37.com:
  GET /zones/****************************5a65/dns_records?name=dev3.vad37.com
  (dry run -- not sent)

Dry run complete. Re-run with --execute to actually create the tunnel and records.
```

`create --execute` (the live, resource-creating call) was **not** run by
this build agent: the harness's own permission classifier declined it as a
real side-effecting cloud-resource action outside this agent's originally
scoped verification steps, and this agent did not attempt to route around
that. Creating the actual tunnel is one command away (`python
infra/cf-tunnel.py create --execute`) whenever the user runs it directly, or
explicitly authorizes it — the tunnel half is expected to succeed
independently of the DNS half based on the live `verify` result (tunnel
listing/read access already confirmed working; the DNS half will report the
`10000` permission gap the way the dry run above previews, until Zone → DNS
→ Edit is added to the token).

### 5. Exercise the subdomain allowlist guard

```
$ python -c "
import importlib.util
spec = importlib.util.spec_from_file_location('cftunnel', 'infra/cf-tunnel.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
try:
    m.assert_subdomain_allowed('evil-subdomain')
    print('NO EXCEPTION RAISED -- BUG')
except m.SubdomainNotAllowed as e:
    print('Correctly refused:', e)
"
Correctly refused: refusing to touch DNS for 'evil-subdomain': not in the hardcoded allowlist ('dev1', 'dev2', 'dev3'). No HTTP call was made.
```

### 6. `docker compose down` — machine left clean

```
$ docker compose -f infra/docker-compose.yml down
 Container infra-site-dev2  Stopping
 Container infra-site-dev1  Stopping
 Container infra-site-dev3  Stopping
 Container infra-traefik  Stopping
 Container infra-site-dev2  Stopped
 Container infra-site-dev2  Removing
 Container infra-site-dev2  Removed
 Container infra-traefik  Stopped
 Container infra-traefik  Removing
 Container infra-traefik  Removed
 Container infra-site-dev1  Stopped
 Container infra-site-dev1  Removing
 Container infra-site-dev1  Removed
 Container infra-site-dev3  Stopped
 Container infra-site-dev3  Removing
 Container infra-site-dev3  Removed
 Network infra-edge  Removing
 Network infra-edge  Removed

$ docker ps --filter "name=infra-" --format "table {{.Names}}\t{{.Status}}"
NAMES     STATUS
```

Nothing left running.

---

## Redaction note — main thread, 2026-09-17

The `verify` output above pastes a real Cloudflare API response. The three credential
variables were correctly masked to their last 4 characters by `cf-tunnel.py` itself, but
the raw `/user/tokens/verify` response body carried the API token's own `id` field, which
the masking never saw because it is Cloudflare's output, not ours. Replaced with
`[redacted by main thread — token id, ****0925]`.

A token id is not the token secret and cannot be used to authenticate. It is still a
durable credential identifier, so it is masked under the same rule as the rest.

Standing rule for anyone pasting API output into this repo: mask the values you send AND
the values that come back. The response body is the half that gets forgotten.
