# RAW — Vietnam Law on Artificial Intelligence No. 134/2025/QH15, PRIMARY TEXT

Wave 2a-bis (re-pick). All pulls 2026-09-17. This closes the highest-value open item left by wave 2b,
which had only law-firm secondary readings (`review-buyer-trigger-pulls.md` PULLs 4-5) and recorded
`thuvienphapluat.vn 403` for the statute text.

---

## PULL 1 — locating the document on the government gazette portal

SOURCE: Cổng thông tin điện tử Chính phủ — hệ thống văn bản (vanban.chinhphu.vn)
URL: https://vanban.chinhphu.vn/?pageid=27160&docid=216334
PULL DATE: 2026-09-17
METHOD: `curl` direct fetch. WebSearch quota was exhausted (200/200) for this session, and
`vbpl.vn` / `phapluat.gov.vn` are now client-rendered Next.js SPAs that return a loading shell to curl.
The portal's own list pages (`he-thong-van-ban?classid=...`) return HTTP 500 "Server bận do đang bảo trì".
Only the per-document detail page works. The docid was found by sweeping docid ranges and matching
`<title>` — recorded here so a later pass does not repeat the sweep.

VERBATIM metadata block, as rendered:

```
Luật số 134/2025/QH15 của Quốc hội: Luật Trí tuệ nhân tạo
Số ký hiệu
 134/2025/QH15
Ngày ban hành
 10-12-2025
Ngày có hiệu lực
 01-03-2026
Loại văn bản
 Luật
Cơ quan ban hành
 Quốc hội
Người ký
 Trần Thanh Mẫn
Trích yếu
 Luật Trí tuệ nhân tạo
Tài liệu đính kèm
luat134.signed.pdf
```

Attachment URL: https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/luat134.signed.pdf
(HTTP 200, 1,060,110 bytes, PDF 1.4, 20 pages, signed "CỔNG THÔNG TIN ĐIỆN TỬ CHÍNH PHỦ … Thời gian ký: 12.01.2026 16:08:23 +07:00")

---

## PULL 2 — the statute text itself

SOURCE: `luat134.signed.pdf` (the gazette PDF from PULL 1)
URL: https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/luat134.signed.pdf
PULL DATE: 2026-09-17
METHOD: downloaded with `curl`; the PDF carries **no text layer** (`pdftotext` returns only the
digital-signature block), so the 20 pages were rendered to PNG with `pypdfium2` at scale 2.2 and
transcribed visually. Transcription is by this agent from the rendered page images — a human-readable
scan, not an extracted text layer. Pages transcribed: 1, 2, 4, 5, 6, 7, 8, 9, 19, 20. Pages 3, 10-18
were rendered but not transcribed this pass (`unknown — not transcribed 2026-09-17`); they cover
Điều 6-7 and Điều 16-30 (development promotion, controlled sandbox, human resources, data, state
management).

### Page 1 — title, scope, definitions

> QUỐC HỘI
> Luật số: 134/2025/QH15
> CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
> Độc lập - Tự do - Hạnh phúc
>
> LUẬT
> TRÍ TUỆ NHÂN TẠO
>
> Căn cứ Hiến pháp nước Cộng hòa xã hội chủ nghĩa Việt Nam đã được sửa đổi, bổ sung một số điều theo Nghị quyết số 203/2025/QH15;
> Quốc hội ban hành Luật Trí tuệ nhân tạo.
>
> Chương I — QUY ĐỊNH CHUNG
>
> Điều 1. Phạm vi điều chỉnh
> 1. Luật này quy định về nghiên cứu, phát triển, cung cấp, triển khai và sử dụng hệ thống trí tuệ nhân tạo (sau đây gọi là hoạt động trí tuệ nhân tạo); quyền, nghĩa vụ của tổ chức, cá nhân có liên quan và quản lý nhà nước đối với hoạt động trí tuệ nhân tạo tại Việt Nam.
> 2. Hoạt động trí tuệ nhân tạo chỉ phục vụ cho mục đích quốc phòng, an ninh, cơ yếu không thuộc phạm vi điều chỉnh của Luật này.
>
> Điều 2. Đối tượng áp dụng
> Luật này áp dụng đối với cơ quan, tổ chức, cá nhân Việt Nam và tổ chức, cá nhân nước ngoài tham gia vào hoạt động trí tuệ nhân tạo tại Việt Nam.
>
> Điều 3. Giải thích từ ngữ
> […]
> 3. *Nhà phát triển* là tổ chức, cá nhân thực hiện việc thiết kế, xây dựng, huấn luyện, kiểm thử hoặc tinh chỉnh toàn bộ hoặc một phần mô hình, thuật toán hoặc hệ thống trí tuệ nhân tạo và có quyền kiểm soát trực tiếp đối với phương pháp kỹ thuật, dữ liệu huấn luyện hoặc tham số mô hình.
> 4. *Nhà cung cấp* là tổ chức, cá nhân đưa hệ thống trí tuệ nhân tạo ra thị trường hoặc đưa vào sử dụng dưới tên, thương hiệu hoặc nhãn hiệu của mình, không phụ thuộc hệ thống đó do họ tự phát triển hay được phát triển bởi bên thứ ba.

### Page 2 — more definitions, basic principles

> 5. *Bên triển khai* là tổ chức, cá nhân sử dụng hệ thống trí tuệ nhân tạo thuộc phạm vi kiểm soát của mình trong hoạt động nghề nghiệp, thương mại hoặc cung cấp dịch vụ; không bao gồm trường hợp sử dụng cho mục đích cá nhân, phi thương mại.
> […]
> 8. *Sự cố nghiêm trọng* là sự kiện xảy ra trong hoạt động của hệ thống trí tuệ nhân tạo, gây ra hoặc có nguy cơ gây ra thiệt hại đáng kể đến tính mạng, sức khỏe, quyền con người, tài sản, an ninh mạng, trật tự công cộng, môi trường hoặc làm gián đoạn hoạt động của hệ thống thông tin quan trọng về an ninh quốc gia.
>
> Điều 4. Nguyên tắc cơ bản trong hoạt động trí tuệ nhân tạo
> […]
> 3. Bảo đảm công bằng, minh bạch, không thiên lệch, không phân biệt đối xử và không gây hại cho con người hoặc xã hội; tuân thủ chuẩn mực đạo đức và giá trị văn hóa Việt Nam; thực hiện trách nhiệm giải trình về các quyết định và hệ quả của hệ thống trí tuệ nhân tạo.

### Page 4 — prohibited purposes, and the one-stop portal

> 2. Phát triển, cung cấp, triển khai hoặc sử dụng các hệ thống trí tuệ nhân tạo nhằm mục đích sau đây:
> a) Thực hiện các hành vi bị nghiêm cấm theo quy định của luật;
> b) Sử dụng yếu tố giả mạo hoặc mô phỏng người, sự kiện thật để lừa dối hoặc thao túng nhận thức, hành vi của con người một cách có chủ đích và có hệ thống, gây tổn hại nghiêm trọng đến quyền, lợi ích hợp pháp của con người;
> c) Lợi dụng điểm yếu của nhóm người dễ bị tổn thương, bao gồm trẻ em, người cao tuổi, người khuyết tật, người dân tộc thiểu số hoặc người mất năng lực hành vi dân sự, người bị hạn chế năng lực hành vi dân sự, người có khó khăn trong nhận thức, làm chủ hành vi để gây tổn hại cho chính họ hoặc người khác;
> d) Tạo ra hoặc phổ biến nội dung giả mạo có khả năng gây nguy hại nghiêm trọng đến an ninh quốc gia, trật tự, an toàn xã hội.
> 3. Thu thập, xử lý hoặc sử dụng dữ liệu để phát triển, huấn luyện, kiểm thử hoặc vận hành hệ thống trí tuệ nhân tạo trái với quy định của pháp luật về dữ liệu, bảo vệ dữ liệu cá nhân, sở hữu trí tuệ và an ninh mạng.
> 4. Cản trở, vô hiệu hóa hoặc làm sai lệch cơ chế giám sát, can thiệp và kiểm soát của con người đối với hệ thống trí tuệ nhân tạo theo quy định của Luật này.
> 5. Che giấu thông tin bắt buộc phải công khai, minh bạch hoặc giải trình; tẩy xóa, làm sai lệch các thông tin, nhãn, cảnh báo bắt buộc trong hoạt động trí tuệ nhân tạo.
> 6. Lợi dụng hoạt động nghiên cứu, thử nghiệm, đánh giá hoặc kiểm định hệ thống trí tuệ nhân tạo để thực hiện hành vi trái quy định của luật.
>
> Điều 8. Cổng thông tin điện tử một cửa về trí tuệ nhân tạo và Cơ sở dữ liệu quốc gia về hệ thống trí tuệ nhân tạo
> 1. Cổng thông tin điện tử một cửa về trí tuệ nhân tạo là nền tảng số được thiết lập nhằm hỗ trợ việc tiếp nhận, đăng ký tham gia thử nghiệm có kiểm soát; tiếp nhận thông báo kết quả phân loại hệ thống trí tuệ nhân tạo, báo cáo sự cố nghiêm trọng và báo cáo định kỳ; công khai thông tin về hệ thống trí tuệ nhân tạo, kết quả đánh giá sự phù hợp, kết quả xử lý vi phạm theo quy định của pháp luật và kết nối các chương trình hỗ trợ, quỹ, hạ tầng, dữ liệu dùng chung.

### Page 5 — Chương II, the risk tiers (Điều 9) and the notification duty (Điều 10)

> Chương II — PHÂN LOẠI VÀ QUẢN LÝ HỆ THỐNG TRÍ TUỆ NHÂN TẠO THEO RỦI RO
>
> Điều 9. Phân loại mức độ rủi ro của hệ thống trí tuệ nhân tạo
> 1. Hệ thống trí tuệ nhân tạo được phân loại theo các mức độ rủi ro sau đây:
> a) Hệ thống trí tuệ nhân tạo có rủi ro cao là hệ thống có thể gây thiệt hại đáng kể đến tính mạng, sức khỏe, quyền và lợi ích hợp pháp của tổ chức, cá nhân, lợi ích quốc gia, lợi ích công cộng, an ninh quốc gia;
> b) Hệ thống trí tuệ nhân tạo có rủi ro trung bình là hệ thống có khả năng gây nhầm lẫn, tác động hoặc thao túng người sử dụng do không nhận biết được chủ thể tương tác là hệ thống trí tuệ nhân tạo hoặc nội dung do hệ thống tạo ra;
> c) Hệ thống trí tuệ nhân tạo có rủi ro thấp là hệ thống không thuộc trường hợp quy định tại điểm a và điểm b khoản này.
> 2. Việc phân loại rủi ro của hệ thống trí tuệ nhân tạo được xác định trên cơ sở các tiêu chí về mức độ tác động đến quyền con người, an toàn, an ninh; lĩnh vực sử dụng của hệ thống, đặc biệt là lĩnh vực thiết yếu hoặc liên quan trực tiếp đến lợi ích công cộng; phạm vi người sử dụng và quy mô ảnh hưởng của hệ thống.
> 3. Chính phủ quy định chi tiết Điều này.
>
> Điều 10. Phân loại và thông báo hệ thống trí tuệ nhân tạo
> 1. Nhà cung cấp tự phân loại hệ thống trí tuệ nhân tạo trước khi đưa vào sử dụng. Hệ thống được phân loại là rủi ro trung bình hoặc rủi ro cao phải có hồ sơ phân loại kèm theo.
> 2. Bên triển khai được kế thừa kết quả phân loại của nhà cung cấp và có trách nhiệm bảo đảm an toàn, nguyên vẹn của hệ thống trong quá trình sử dụng; trường hợp sửa đổi, tích hợp hoặc thay đổi chức năng làm phát sinh rủi ro mới hoặc rủi ro cao hơn thì phối hợp nhà cung cấp thực hiện phân loại lại.
> 3. Đối với hệ thống được phân loại là rủi ro trung bình hoặc rủi ro cao, nhà cung cấp phải thông báo kết quả phân loại cho Bộ Khoa học và Công nghệ thông qua Cổng thông tin điện tử một cửa về trí tuệ nhân tạo trước khi đưa vào sử dụng. Khuyến khích tổ chức, cá nhân phát triển hệ thống trí tuệ nhân tạo có rủi ro thấp công khai thông tin cơ bản của hệ thống nhằm tăng tính minh bạch.
> 4. Trường hợp chưa xác định được mức độ rủi ro, nhà cung cấp được đề nghị Bộ Khoa học và Công nghệ hướng dẫn về phân loại trên cơ sở hồ sơ kỹ thuật.
> 5. Việc kiểm tra, giám sát được thực hiện theo mức độ rủi ro của hệ thống:
> a) Hệ thống trí tuệ nhân tạo có rủi ro cao được kiểm tra định kỳ hoặc khi có dấu hiệu vi phạm;
> b) Hệ thống trí tuệ nhân tạo có rủi ro trung bình được giám sát thông qua báo cáo, kiểm tra chọn mẫu hoặc đánh giá của tổ chức độc lập;

### Page 6 — low-risk supervision, transparency (Điều 11), incident duty (Điều 12)

> c) Hệ thống trí tuệ nhân tạo có rủi ro thấp được theo dõi, kiểm tra khi có sự cố, phản ánh hoặc khi cần bảo đảm an toàn, không làm phát sinh nghĩa vụ không cần thiết cho tổ chức, cá nhân.
> 6. Trên cơ sở kết quả kiểm tra, giám sát quy định tại khoản 5 Điều này, khi phát hiện sai lệch hoặc khai báo không trung thực, cơ quan có thẩm quyền yêu cầu tái phân loại, bổ sung hồ sơ hoặc tạm dừng việc sử dụng, đồng thời xử lý theo quy định của pháp luật.
> 7. Chính phủ quy định chi tiết về nội dung cần thông báo, trình tự, thủ tục thông báo và hướng dẫn kỹ thuật về phân loại rủi ro.
>
> Điều 11. Trách nhiệm minh bạch
> 1. Nhà cung cấp bảo đảm hệ thống trí tuệ nhân tạo tương tác trực tiếp với con người được thiết kế và vận hành để người sử dụng nhận biết khi đang tương tác với hệ thống, trừ trường hợp pháp luật có quy định khác.
> 2. Nhà cung cấp bảo đảm các nội dung âm thanh, hình ảnh, video do hệ thống trí tuệ nhân tạo tạo ra được đánh dấu ở định dạng máy đọc theo quy định của Chính phủ.
> 3. Bên triển khai có trách nhiệm thông báo rõ ràng khi cung cấp ra công cộng văn bản, âm thanh, hình ảnh, video được tạo ra hoặc chỉnh sửa bằng hệ thống trí tuệ nhân tạo nếu nội dung đó có khả năng gây nhầm lẫn về tính xác thực của sự kiện, nhân vật, trừ trường hợp pháp luật có quy định khác.
> […]
> 6. Chính phủ quy định chi tiết hình thức thông báo, gắn nhãn.
>
> Điều 12. Trách nhiệm quản lý và xử lý sự cố trí tuệ nhân tạo
> 1. Nhà phát triển, nhà cung cấp, bên triển khai và người sử dụng hệ thống trí tuệ nhân tạo có trách nhiệm bảo đảm an toàn, an ninh, độ tin cậy và kịp thời phát hiện, khắc phục sự cố có khả năng gây tổn hại đến con người, tài sản, dữ liệu hoặc trật tự xã hội.

### Page 7 — incident handling, and Điều 13, conformity assessment

> 3. Cơ quan quản lý nhà nước có thẩm quyền tiếp nhận, xác minh và hướng dẫn xử lý sự cố; khi cần thiết, có quyền yêu cầu tạm dừng, thu hồi hoặc đánh giá lại hệ thống trí tuệ nhân tạo.
> 4. Báo cáo và xử lý sự cố được thực hiện qua Cổng thông tin điện tử một cửa về trí tuệ nhân tạo.
>
> Điều 13. Đánh giá sự phù hợp đối với hệ thống trí tuệ nhân tạo có rủi ro cao
> 1. Hệ thống trí tuệ nhân tạo có rủi ro cao phải được đánh giá sự phù hợp theo quy định của Luật này trước khi đưa vào sử dụng hoặc khi có thay đổi đáng kể trong quá trình sử dụng. Trường hợp có tiêu chuẩn, quy chuẩn kỹ thuật về hệ thống trí tuệ nhân tạo thì còn phải thực hiện đánh giá sự phù hợp theo quy định của pháp luật về tiêu chuẩn, quy chuẩn kỹ thuật.
> 2. Đánh giá sự phù hợp là việc xác nhận hệ thống trí tuệ nhân tạo đáp ứng các yêu cầu tại Điều 14 của Luật này và được thực hiện như sau:
> a) Đối với hệ thống trí tuệ nhân tạo có rủi ro cao thuộc danh mục hệ thống trí tuệ nhân tạo phải chứng nhận sự phù hợp trước khi đưa vào sử dụng: việc đánh giá được thực hiện bởi tổ chức đánh giá sự phù hợp đã được đăng ký hoặc thừa nhận theo quy định của pháp luật;
> b) Đối với các hệ thống trí tuệ nhân tạo có rủi ro cao khác: nhà cung cấp tự đánh giá sự phù hợp hoặc thuê tổ chức đánh giá sự phù hợp đã được đăng ký hoặc thừa nhận theo quy định của pháp luật.
> 3. Kết quả đánh giá sự phù hợp là điều kiện để hệ thống trí tuệ nhân tạo có rủi ro cao được phép đưa vào sử dụng; tổ chức, cá nhân có hệ thống đã được đánh giá sự phù hợp có trách nhiệm duy trì sự phù hợp và công khai thông tin theo quy định của Chính phủ, là căn cứ để thực hiện kiểm tra, giám sát việc tuân thủ quy định tại Điều 10 của Luật này.
> 4. Thủ tướng Chính phủ quy định Danh mục hệ thống trí tuệ nhân tạo có rủi ro cao, bao gồm danh mục hệ thống trí tuệ nhân tạo phải chứng nhận sự phù hợp trước khi đưa vào sử dụng.
> 5. Tổ chức đánh giá sự phù hợp, kiểm định hệ thống trí tuệ nhân tạo phải bảo đảm tính độc lập, có đủ năng lực kỹ thuật theo quy định và chịu sự giám sát định kỳ của cơ quan nhà nước có thẩm quyền.
> 6. Chính phủ quy định chi tiết Điều này.

### Page 8 — Điều 14, high-risk provider duties

> Điều 14. Quản lý hệ thống trí tuệ nhân tạo có rủi ro cao
> 1. Nhà cung cấp hệ thống trí tuệ nhân tạo có rủi ro cao có trách nhiệm sau đây:
> a) Thiết lập và duy trì biện pháp quản lý rủi ro và thường xuyên rà soát khi hệ thống có thay đổi đáng kể hoặc phát sinh rủi ro mới;
> b) Quản trị dữ liệu huấn luyện, kiểm thử và vận hành bảo đảm chất lượng trong phạm vi khả năng kỹ thuật và phù hợp với mục đích sử dụng của hệ thống;
> c) Lập, cập nhật, lưu giữ hồ sơ kỹ thuật và nhật ký hoạt động ở mức cần thiết cho việc đánh giá sự phù hợp và kiểm tra sau khi đưa vào sử dụng; cung cấp các thông tin này cho cơ quan nhà nước có thẩm quyền theo nguyên tắc cần thiết, tương xứng với mục đích kiểm tra và không làm lộ bí mật kinh doanh;
> d) Thiết kế hệ thống bảo đảm khả năng giám sát và can thiệp của con người đối với hệ thống;
> đ) Thực hiện nghĩa vụ minh bạch và xử lý sự cố theo quy định tại Điều 11 và Điều 12 của Luật này;
> e) Thực hiện trách nhiệm giải trình đối với cơ quan nhà nước có thẩm quyền về mục đích sử dụng, nguyên lý hoạt động ở mức mô tả chức năng, loại dữ liệu đầu vào chủ yếu, biện pháp quản lý và kiểm soát rủi ro cùng các nội dung cần thiết phục vụ thanh tra, kiểm tra […] Việc giải trình và cung cấp thông tin không được yêu cầu tiết lộ mã nguồn, thuật toán chi tiết, bộ tham số hoặc thông tin thuộc bí mật kinh doanh, bí mật công nghệ;
> g) Phối hợp với cơ quan nhà nước có thẩm quyền và bên triển khai trong kiểm tra, đánh giá, hậu kiểm và khắc phục sự cố liên quan đến hệ thống.

### Page 9 — foreign providers, and Điều 15, medium- and low-risk duties

> 6. Nhà cung cấp nước ngoài có hệ thống trí tuệ nhân tạo có rủi ro cao được cung cấp tại Việt Nam phải có đầu mối liên hệ hợp pháp tại Việt Nam; trường hợp hệ thống thuộc diện bắt buộc chứng nhận sự phù hợp trước khi đưa vào sử dụng, phải có hiện diện thương mại hoặc đại diện được ủy quyền tại Việt Nam.
>
> Điều 15. Quản lý hệ thống trí tuệ nhân tạo có rủi ro trung bình và thấp
> 1. Hệ thống trí tuệ nhân tạo có rủi ro trung bình được quản lý như sau:
> a) Nhà cung cấp và bên triển khai phải bảo đảm minh bạch theo quy định tại Điều 11 của Luật này;
> b) Nhà cung cấp có trách nhiệm giải trình về mục đích sử dụng, nguyên lý hoạt động ở mức mô tả chức năng, dữ liệu đầu vào chủ yếu và biện pháp quản lý rủi ro, an toàn của hệ thống khi có yêu cầu của cơ quan nhà nước trong thanh tra, kiểm tra hoặc khi có dấu hiệu rủi ro hoặc sự cố; việc giải trình không yêu cầu tiết lộ mã nguồn, thuật toán chi tiết, bộ tham số hoặc bí mật kinh doanh, bí mật công nghệ;
> c) Bên triển khai có trách nhiệm giải trình về việc vận hành, kiểm soát rủi ro, xử lý sự cố và bảo vệ quyền, lợi ích hợp pháp của tổ chức, cá nhân khi có yêu cầu của cơ quan nhà nước có thẩm quyền trong quá trình thanh tra, kiểm tra hoặc xử lý sự cố;
> d) Người sử dụng có trách nhiệm tuân thủ quy định về thông báo, gắn nhãn hệ thống trí tuệ nhân tạo.
> 2. Hệ thống trí tuệ nhân tạo có rủi ro thấp được quản lý như sau:
> a) Nhà cung cấp có trách nhiệm giải trình khi có yêu cầu của cơ quan nhà nước có thẩm quyền trong trường hợp có dấu hiệu vi phạm pháp luật hoặc ảnh hưởng đến quyền, lợi ích hợp pháp của tổ chức, cá nhân;

### Page 19 — Chương VIII, effective date (Điều 34) and transition (Điều 35)

> Chương VIII — ĐIỀU KHOẢN THI HÀNH
>
> Điều 33. Bãi bỏ một số chương, điều, khoản, điểm của Luật Công nghiệp công nghệ số số 71/2025/QH15
> Bãi bỏ khoản 9 Điều 3, khoản 7 Điều 4, khoản 6 Điều 12, điểm đ khoản 2 Điều 34 và Chương IV của Luật Công nghiệp công nghệ số.
>
> Điều 34. Hiệu lực thi hành
> Luật này có hiệu lực thi hành từ ngày 01 tháng 3 năm 2026, trừ các nội dung liên quan quy định tại Điều 35 của Luật này.
>
> Điều 35. Điều khoản chuyển tiếp
> 1. Đối với các hệ thống trí tuệ nhân tạo đã được đưa vào hoạt động trước ngày Luật này có hiệu lực thi hành, nhà cung cấp và bên triển khai có trách nhiệm thực hiện các nghĩa vụ tuân thủ theo quy định của Luật này trong thời hạn sau đây:
> a) 18 tháng kể từ ngày Luật này có hiệu lực thi hành đối với hệ thống trí tuệ nhân tạo trong lĩnh vực y tế, giáo dục và tài chính;
> b) 12 tháng kể từ ngày Luật này có hiệu lực thi hành đối với các hệ thống

### Page 20 — end of transition, enacting formula

> trí tuệ nhân tạo không thuộc trường hợp quy định tại điểm a khoản này.
> 2. Trong thời hạn quy định tại khoản 1 Điều này, hệ thống trí tuệ nhân tạo được tiếp tục hoạt động, trừ trường hợp cơ quan quản lý nhà nước về trí tuệ nhân tạo xác định hệ thống có nguy cơ gây thiệt hại nghiêm trọng thì có quyền yêu cầu tạm dừng hoặc chấm dứt hoạt động.
>
> Luật này được Quốc hội nước Cộng hòa xã hội chủ nghĩa Việt Nam khóa XV, Kỳ họp thứ 10 thông qua ngày 10 tháng 12 năm 2025.
>
> CHỦ TỊCH QUỐC HỘI
> Trần Thanh Mẫn

---

## PULL 3 — what the primary text does NOT say

METHOD: negative findings from the transcribed pages above, bounded by what was read.

- The words "kiểm thử đối kháng" (adversarial testing), "red team", "đánh giá an toàn nội dung"
  (content-safety evaluation), "guardrail", "jailbreak", and "tiếng Việt" as an evaluation criterion do
  **not** appear on any page transcribed (1, 2, 4-9, 19, 20). `unknown` for pages 3 and 10-18.
- Điều 13 defines *đánh giá sự phù hợp* only as "việc xác nhận hệ thống trí tuệ nhân tạo đáp ứng các
  yêu cầu tại Điều 14" — conformity against Điều 14's **process** duties (risk management, data
  governance, technical dossier, human oversight, transparency, explainability, cooperation). There is
  no performance, accuracy or safety threshold anywhere in Điều 14.
- Điều 9.3, 10.7, 11.6, 13.4 and 13.6 each defer detail to the Government or the Prime Minister. No
  implementing decree, no *Danh mục hệ thống trí tuệ nhân tạo có rủi ro cao*, and no technical guidance
  on risk classification was found on the portal this pass — `unknown — checked vanban.chinhphu.vn
  2026-09-17`; the portal's list pages return HTTP 500, so a decree could exist and not have been seen.
- No penalty article appears in the pages transcribed. Sanctions are referred out ("xử lý theo quy định
  của pháp luật"). `unknown — pages 10-18 not transcribed`.

---

## What this pull settles, and what it does not

SETTLED (primary, filed):

- Law 134/2025/QH15, "Luật Trí tuệ nhân tạo", ban hành 10-12-2025, hiệu lực 01-03-2026. Wave 2b's
  law-firm secondary reading is confirmed on number, name, adoption date and effective date.
- Three risk tiers, **self-classified by the nhà cung cấp** (Điều 10.1), notified to Bộ Khoa học và
  Công nghệ through a one-stop portal before deployment for medium and high (Điều 10.3).
- Medium-risk supervision, verbatim: "báo cáo, kiểm tra chọn mẫu hoặc đánh giá của tổ chức độc lập"
  (Điều 10.5.b). "Đánh giá của tổ chức độc lập" is one of three alternatives available to the
  **regulator**, not a duty imposed on the provider. Wave 2b's secondary source rendered this as
  "sample audits or assessments by independent organizations" — accurate, but the grammatical subject
  matters and the secondary reading obscured it.
- Third-party conformity assessment is mandatory **only** for high-risk systems on a Prime-Minister
  list that does not yet exist (Điều 13.2.a + 13.4). Other high-risk systems may self-assess
  (Điều 13.2.b). Assessment bodies must be "đã được đăng ký hoặc thừa nhận theo quy định của pháp luật"
  and "bảo đảm tính độc lập, có đủ năng lực kỹ thuật theo quy định" (Điều 13.5) — a registration regime
  whose conditions are not in the statute.
- Transition: 12 months from 2026-03-01 (→ **2027-03-01**) for systems already deployed; 18 months
  (→ **2027-09-01**) for health, education and finance. Wave 2b had these the right way round.
- Transparency (Điều 11) binds any system interacting directly with humans, at every risk tier, and is
  the *definition* of the medium tier (Điều 9.1.b: "gây nhầm lẫn … do không nhận biết được chủ thể
  tương tác là hệ thống trí tuệ nhân tạo").

NOT SETTLED:

- The risk tier of a Vietnamese-language consumer chatbot. Điều 9.1.b's wording fits a system whose
  users may not realise they are talking to an AI; a chatbot that discloses itself under Điều 11.1
  arguably falls into 9.1.c (low). This is an inference either way and the statute does not decide it.
  Điều 9.3 hands it to the Government.
- Whether any assessment methodology will mention content safety, adversarial testing or language
  coverage. Nothing in the transcribed text does.
- Penalties. Not in the pages read.

---

## PULL 4 — attempt to locate the one-stop AI portal mandated by Điều 8

SOURCE: direct hostname probes plus the Bộ Khoa học và Công nghệ portal
PULL DATE: 2026-09-17
METHOD: `curl -L -A "Mozilla/5.0"` against six candidate hostnames, then the MOST site.

```
200 140940  https://mst.gov.vn          Trang chủ - Cổng Thông tin điện tử Bộ Khoa học và Công nghệ
000 0       https://ai.mst.gov.vn       (DNS failure)
000 0       https://aiportal.mst.gov.vn (DNS failure)
000 0       https://mocua.ai.gov.vn     (DNS failure)
000 0       https://ai.gov.vn           (DNS failure)
000 0       https://tri-tue-nhan-tao.mst.gov.vn (DNS failure)
```

A keyword query against `mst.gov.vn/tim-kiem` returned the homepage byte-for-byte (140,940 bytes),
i.e. that path is not a search endpoint. The only AI-related item surfaced on the MOST homepage,
verbatim: "Quỹ Đổi mới công nghệ quốc gia (NATIF) thông báo tiếp nhận hồ sơ đề nghị tài trợ nhiệm vụ
đổi mới công nghệ ứng dụng trí tuệ nhân tạo (AI) năm 2026. Mức tài trợ từ ngân sách nhà nước tối đa
3 tỷ đồng/nhiệm vụ; thời gian thực hiện không quá 12 tháng." — a technology-innovation grant
announcement, unrelated to Điều 8.

RESULT: `unknown — checked six candidate hostnames and mst.gov.vn 2026-09-17, portal not located`.
This is a shallow probe with no browser and no search budget. It is NOT evidence that the portal does
not exist. It is recorded because Điều 8.1 obliges that portal to publish classification results and
conformity-assessment results, which would make the number of notified medium- and high-risk systems a
directly countable, primary demand figure — and because nobody in this repo has looked for it.
