# Who the Vietnamese advertising law binds, and what it asks them to do — raw pull

Pulled: 2026-09-17, wave 2b. Method: local text extraction from `raw/vn-luat-quang-cao-2012-full-text.txt` (wave 1b's pull of Luật 16/2012/QH13 from the official Government portal `vanban.chinhphu.vn`), cross-read against `raw/vn-luat-75-2025-dieu23-quang-cao-tren-mang.txt` (wave 1b's transcription of the replacement Điều 23 from the signed PDF at `datafiles.chinhphu.vn`). No new network fetch — this pull extracts provisions wave 1b's addendum cited but did not quote: **the definitions of the four duty-bearers, and the duties Điều 23.3 imports.** Vietnamese verbatim, translation mine.

Wave 1b established *what* the 2025 amendment requires. This pull establishes *who* it requires it of, which is the question that decides whether the law reaches this project's founders.

---

## 1. The four duty-bearers — Điều 2, Luật 16/2012/QH13, verbatim

> "5. **Người quảng cáo** là tổ chức, cá nhân có yêu cầu quảng cáo sản phẩm, hàng hóa, dịch vụ của mình hoặc bản thân tổ chức, cá nhân đó."

Translation (mine): "**The advertiser** is an organisation or individual that requires advertising of its products, goods, services, or of itself."

> "6. **Người kinh doanh dịch vụ quảng cáo** là tổ chức, cá nhân thực hiện một, một số hoặc tất cả các công đoạn của quá trình quảng cáo theo hợp đồng cung ứng dịch vụ quảng cáo với người quảng cáo."

Translation (mine): "**The advertising service business** is an organisation or individual performing **one, some, or all stages of the advertising process** under an advertising-service supply contract with the advertiser."

> "7. **Người phát hành quảng cáo** là tổ chức, cá nhân dùng phương tiện quảng cáo thuộc trách nhiệm quản lý của mình giới thiệu sản phẩm quảng cáo đến công chúng, bao gồm cơ quan báo chí, nhà xuất bản, chủ trang thông tin điện tử, người tổ chức chương trình văn hóa, thể thao và tổ chức, cá nhân sử dụng phương tiện quảng cáo khác."

Translation (mine): "**The advertising publisher** is an organisation or individual that uses **an advertising medium under its own management responsibility** to introduce the advertising product to the public, including press agencies, publishers, **owners of electronic information pages**, cultural/sports programme organisers, and organisations or individuals using other advertising media."

> "8. **Người chuyển tải sản phẩm quảng cáo** là người trực tiếp đưa các sản phẩm quảng cáo đến công chúng hoặc thể hiện sản phẩm quảng cáo trên người thông qua hình thức mặc, treo, gắn, dán, vẽ hoặc các hình thức tương tự."

Translation (mine): "**The conveyor of the advertising product** is a person who directly brings advertising products to the public or displays advertising products on their person by wearing, hanging, attaching, sticking, drawing or similar forms."

> "9. **Người tiếp nhận quảng cáo** là người tiếp nhận thông tin từ sản phẩm quảng cáo thông qua phương tiện quảng cáo."

Translation (mine): "**The advertising recipient** is a person who receives information from an advertising product through an advertising medium."

Also relevant, Điều 2.4:

> "4. **Xúc tiến quảng cáo** là hoạt động tìm kiếm, thúc đẩy cơ hội ký kết hợp đồng dịch vụ quảng cáo."
Translation (mine): "**Advertising promotion** is the activity of seeking and promoting opportunities to sign advertising-service contracts."

And Điều 2.1, already quoted in wave 1b's addendum, which excludes news/current-affairs content from the definition of advertising.

## 2. What Điều 23.3 (2025 amendment) does with those definitions — verbatim

From `raw/vn-luat-75-2025-dieu23-quang-cao-tren-mang.txt`:

> "3. **Người quảng cáo, người kinh doanh dịch vụ quảng cáo, người phát hành quảng cáo, người chuyển tải sản phẩm quảng cáo** tham gia hoạt động quảng cáo trên mạng có quyền, nghĩa vụ theo quy định tại **các điều 12, 13, 14 và 15a** của Luật này và phải tuân thủ:
> a) Quy định của pháp luật về quảng cáo, an ninh mạng, bảo vệ dữ liệu cá nhân, bảo vệ quyền lợi người tiêu dùng, bảo vệ trẻ em, quản lý, cung cấp, sử dụng dịch vụ Internet và thông tin trên mạng; **phải đăng ký thuế, kê khai, nộp thuế đối với doanh thu phát sinh từ dịch vụ quảng cáo** theo quy định của pháp luật về thuế;"

Translation (mine): "3. The advertiser, the advertising service business, the advertising publisher, and the conveyor of the advertising product taking part in online advertising activity have the rights and obligations provided in **Articles 12, 13, 14 and 15a** of this Law, and must comply with: a) the law on advertising, cybersecurity, personal data protection, consumer protection, child protection, and the management/provision/use of Internet services and online information; **must register for tax, declare and pay tax on revenue arising from advertising services** per tax law;"

## 3. The two duties in Điều 23.2 that a generated answer has no surface for

> "a) **Phải có dấu hiệu nhận diện rõ ràng** bằng chữ số, chữ viết, ký hiệu, hình ảnh, âm thanh **để phân biệt giữa nội dung quảng cáo với các nội dung khác không phải quảng cáo**;"

Translation (mine): "a) There **must be a clear identification sign** — by number, letter, symbol, image or sound — **to distinguish advertising content from other, non-advertising content**;"

> "b) Đối với những quảng cáo không ở vùng cố định, **phải có tính năng, biểu tượng dễ nhận biết cho phép người tiếp nhận quảng cáo tắt quảng cáo, thông báo nội dung quảng cáo vi phạm cho nhà cung cấp dịch vụ, từ chối xem nội dung quảng cáo không phù hợp**;"

Translation (mine): "b) For advertising not in a fixed area, there **must be an easily recognisable feature or icon allowing the advertising recipient to turn the advertisement off, report violating advertising content to the service provider, and refuse to view unsuitable advertising content**;"

## 4. The duty that requires a medium you manage — Điều 14, Luật 16/2012/QH13, verbatim

> "Điều 14. Quyền và nghĩa vụ của người phát hành quảng cáo
> 1. Được quảng cáo trên **phương tiện của mình** và thu phí dịch vụ theo quy định của pháp luật.
> 2. Kiểm tra các tài liệu liên quan đến điều kiện quảng cáo của tổ chức, cá nhân, sản phẩm, hàng hóa, dịch vụ cần quảng cáo.
> 3. **Cung cấp tài liệu liên quan đến sản phẩm quảng cáo khi người tiếp nhận quảng cáo hoặc cơ quan nhà nước có thẩm quyền yêu cầu.**
> 4. Thực hiện hợp đồng phát hành quảng cáo đã ký kết và **chịu trách nhiệm trực tiếp về sản phẩm quảng cáo thực hiện trên phương tiện quảng cáo thuộc trách nhiệm quản lý của mình.**"

Translation (mine): "Article 14. Rights and obligations of the advertising publisher. 1. May advertise on **its own medium** and collect service fees per law. 2. Must check the documents relating to the advertising conditions of the organisation, individual, product, goods or service to be advertised. 3. **Must provide documents relating to the advertising product when the advertising recipient or a competent state agency requests them.** 4. Must perform the signed advertising-publication contract and **bear direct responsibility for the advertising product carried on the advertising medium under its own management responsibility.**"

And Điều 12.2(a), the advertiser's obligation, verbatim:

> "a) Cung cấp cho người kinh doanh dịch vụ quảng cáo hoặc người phát hành quảng cáo thông tin cần thiết, trung thực, chính xác về cơ quan, tổ chức, cá nhân, sản phẩm, hàng hóa, dịch vụ, các tài liệu liên quan đến điều kiện quảng cáo và chịu trách nhiệm về các thông tin đó;"

Điều 13 sets out the advertising service business's rights and obligations; its obligation list opens, verbatim: "a) Hoạt động theo đúng phạm vi, lĩnh vực đã đư[ợc]..." ("operate strictly within the scope and field it has been [permitted]...").

---

## Read, stated once

The statute allocates every online-advertising duty to one of four named roles, and two of those roles are defined **by reference to a medium the duty-bearer manages** (Điều 2.7: "phương tiện quảng cáo thuộc trách nhiệm quản lý của mình"; Điều 14.1: "phương tiện của mình"; Điều 14.4, direct responsibility for what is carried on that medium).

A Vietnam-based two-person team taking payment from a brand to place product-placement text is, on Điều 2.6's text, a "người kinh doanh dịch vụ quảng cáo" — it performs "một, một số hoặc tất cả các công đoạn của quá trình quảng cáo" under a service contract with the advertiser. Điều 23.3 then binds it to Điều 13 and to all of Điều 23.2.

Điều 23.2(a) requires the identification sign to reach the "người tiếp nhận quảng cáo" (Điều 2.9 — the person who receives the information through the advertising medium). Điều 23.2(b) additionally requires an off-switch, a report-to-service-provider control, and a refusal control. When the placement is rendered inside a third party's generated answer, the founders manage no surface in the recipient's experience on which any of these can be placed, and Điều 14.3's duty to hand documents to a requesting recipient cannot be performed by anyone the recipient can identify.

`unknown — checked vanban.chinhphu.vn 2026-09-17`: the text of the newly-inserted **Điều 15a** (imported by Điều 23.3) was not located — it is added by the 2025 amendment and does not appear in the 2012 base text; wave 1b's transcription of Điều 23 truncates before it. The implementing decree under Điều 23.8 remains unlocated, as wave 1b recorded.

## Caveats

- Translations are mine and are not certified. The Vietnamese is the operative text.
- No penalty provision, administrative-fine decree, or enforcement case was pulled. What happens to a non-compliant "người kinh doanh dịch vụ quảng cáo" in practice is `unknown — not pulled 2026-09-17`.
- Điều 13's full obligation list was extracted only to its first clause. Điều 15a is unread.
- Whether a ChatGPT or Gemini answer is a "phương tiện quảng cáo" or a "nền tảng số có kết nối Internet" within Điều 23.1 is a question of statutory interpretation this pull does not and cannot settle. What it does settle is the allocation of duties, which holds either way.
- Nothing in the 2012 law or the 2025 amendment mentions crawlers, bots, AI, or differential serving. Wave 1b's finding on that point is re-confirmed, not extended.
