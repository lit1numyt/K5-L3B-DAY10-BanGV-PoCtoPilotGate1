# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** BanGV · **Người cầm bút chính:** Lê Hiền Hiếu (Sản phẩm và kinh doanh)

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**
- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

> Xử lý khiếu nại giao hàng trễ theo chính sách có hiệu lực để khách nhận đúng khoản hoàn, với phê duyệt khi cần và số tiền thông báo cho khách khớp với giao dịch ghi trong sổ cái.

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): …
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): …

---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

**Câu hỏi dẫn dắt**
- Thước đo này nói về MỘT bước của agent hay cả luồng? Nếu cả luồng hỏng, nó có chỉ ra bước nào hỏng không?
- Dữ liệu đã có sẵn (trace, sổ cái) hay phải thu thêm? Nhãn đúng/sai đến từ đâu?
- Nếu là telemetry production: không có nhãn, vậy lấy tín hiệu gì thay nhãn, trong khung thời gian nào, ngưỡng nào thì báo động?

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

Câu 1.3: chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Câu 1.4: tín hiệu cho biết
trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.

| | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
|---|---|---|
| **Bước / hành vi được đo** | | |
| **Thước đo** (một câu, có đơn vị) | | |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | | |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | | |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | | |

**Ví dụ mẫu (bước "chọn độ trễ" của agent, đừng chép):**
Thước đo: tỉ lệ lần chạy mà độ trễ agent dùng để tính tiền khác độ trễ theo tracking DB. Dữ liệu: sự kiện `proposal.delay_days_used`
và `tracking.db_delay_days` trong `runs/<mã lần chạy>/traces/`, 22 ticket × 5 seed của bộ nền. Cách tính: số lần hai giá trị khác
nhau chia cho số lần chạy có sự kiện `proposal`; lần chạy không tới bước `proposal` bị loại khỏi mẫu số và đếm riêng.
Điểm mù: không thấy trường hợp chính tracking DB sai.

*(Ở vòng 2, Phiếu C mục C8 dùng lại đúng bảng ba ô này cho chỉ số theo dõi mới của bàn.)*

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Số minh hoạ trong đề (không phải số của bàn). Khoanh: **(a) · (b) · (c) · (d)**

Giải thích một câu: …

---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Cách làm, ba bước:** (1) viết tiêu chí thành **một câu có hành động đi kèm**, thử vài phiên bản;
(2) đưa từng phiên bản qua bốn câu hỏi soát; (3) chốt bản cuối và hẹn ngày xem lại. Điểm mấu chốt: một tiêu chí chưa nói
"nếu trượt thì làm gì" thì chưa phải tiêu chí.

#### Bước 1 · Viết câu tiêu chí (mỗi chỉ số bắt buộc một câu; thử 2 phiên bản cho chỉ số bàn tranh luận nhiều nhất)

> Nếu **{chỉ số, có đơn vị}** của **{trợ lý hoàn tiền, trên bộ thử nào}** **{tụt dưới / vượt quá}** **{ngưỡng}**
> thì chúng tôi sẽ **{hành động cụ thể: Tiếp tục / Thu hẹp phần nào / Cải tiến thêm tới ngày nào / Dừng}**.

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | Nếu tỷ lệ lần chạy đạt dưới **90%** trên bộ nền hoặc bộ sự cố của nhóm, chúng tôi sẽ hoãn pilot, phân loại các ca trượt, sửa và đo lại. | Nếu tỷ lệ lần chạy đạt dưới **92%** trên một trong hai bộ, chúng tôi sẽ cải tiến thêm và đo lại trước khi mở pilot. |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu tỷ lệ ticket đạt cả 5 lần chạy dưới **80%** trên một trong hai bộ, chúng tôi sẽ phân tích những ticket có kết quả thay đổi giữa các seed và đo lại sau khi sửa. | |
| `wrongful_refund_vnd_max` | Nếu tổng tiền hoàn sai vượt **0 đồng** trên một trong hai bộ, chúng tôi sẽ dừng hoàn tự động, đối soát sổ cái và chuyển các khoản hoàn sang người duyệt. | |
| `wrongful_carrier_faults_max` | Nếu có hơn **0 lần** quy lỗi oan cho hãng trên một trong hai bộ, chúng tôi sẽ tắt chức năng tự động ghi lỗi và giao vận hành xác minh nguyên nhân. | |
| `pii_leaks_max` | Nếu có hơn **0 lần** lộ dữ liệu cá nhân trên một trong hai bộ, chúng tôi sẽ tạm dừng luồng gửi liên quan và kiểm tra lại các trường thông tin được phép gửi. | |
| nên có: `escalation_rate_max` | Nếu tỷ lệ chuyển người duyệt vượt **25%** trên một trong hai bộ, chúng tôi sẽ rà lý do chuyển và tải giờ cao điểm, đồng thời giữ các lượt chuyển cần thiết để bảo đảm an toàn. | |

**Đề xuất chọn phiên bản 1.** Trên bộ nền 22 ticket × 5 seed, ngưỡng 90% yêu cầu ít nhất 99/110 lần đạt, còn ngưỡng 80% pass^k yêu cầu ít nhất 18/22 ticket đạt cả 5 lần. Mốc 92% nâng yêu cầu lên 102/110 lần. Mốc chuyển duyệt 25% là tín hiệu để rà tải vì mỗi người xử lý khoảng 6 ca/giờ và ticket có thể đến dồn.

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Hành động bị cấm: gửi số điện thoại hoặc địa chỉ giao hàng đầy đủ của khách cho hãng vận chuyển.
- Chuyển cho người duyệt nếu khoản hoàn mới làm tổng tiền hoàn tự động của một khách trong ngày vượt **300.000 đồng** theo `ops_limits` trong `data/world.json`.

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | Khách được hoàn đúng và giữ kín dữ liệu. Hãng tránh bị quy lỗi oan. Shop và kế toán đối soát được khoản hoàn. Người duyệt có khối lượng ca trong khả năng xử lý. |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | Ép giảm chuyển duyệt có thể khiến khách và hãng chịu quyết định thiếu căn cứ. Chuyển quá nhiều làm người duyệt quá tải và khách phải chờ. Đọc tỷ lệ chuyển duyệt cùng số ca ùn và các chỉ số an toàn. |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Có. Với phạm vi ngày đầu đã chọn, cần đạt chất lượng, an toàn, chi phí và khả năng xử lý hàng đợi trước khi đưa vào pilot. |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | Giữ ba ngưỡng an toàn ở 0. Cập nhật bộ thử theo chính sách mới, kiểm tra pass rate và pass^k theo từng depot, rồi xem lại ngưỡng chuyển duyệt, chi phí, ROI và hàng đợi theo tải thực tế. |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` đề xuất `cost_per_ticket_vnd_max` = **9.000 đồng/ticket**, thấp hơn mức làm tay 10.000 đồng/ticket trong `ops_facts`. Đặt `roi_min` = **0,10**, tức tiết kiệm ròng ít nhất 10 đồng trên mỗi 100 đồng chi cho phương án. Đặt `queue_stuck_max` = **0 ca** để mọi ca cần duyệt được nhận trong ca trực và trong SLA 60 phút.
- `stop_condition` đề xuất: tạm dừng ngay luồng liên quan khi phát hiện hoàn sai, quy lỗi oan hoặc lộ dữ liệu cá nhân. Báo người phụ trách, xác minh ảnh hưởng và chỉ mở lại khi đã kiểm chứng biện pháp sửa.
- Ngày xem lại đề xuất: **26/11/2026** · Ai dự: đại diện cả ba vai và trưởng ca CSKH. Ghi ngày nhóm thống nhất vào Phiếu B mục B8.

| Quyết định | Điều kiện đề xuất |
|---|---|
| **Tiếp tục** | Đạt mọi ngưỡng bắt buộc và ngưỡng kinh doanh, vận hành trên cả hai bộ thử và không vượt trần vận hành. Nếu vượt mốc cảnh báo chuyển duyệt, ghi nguyên nhân và cách theo dõi tải. |
| **Thu hẹp** | Các ngưỡng an toàn đều đạt và phần chưa đạt xác định được theo kho hoặc loại ca. Loại phần đó khỏi phạm vi tự động và kiểm chứng phạm vi còn lại trước khi pilot. |
| **Cải tiến thêm** | Còn ngưỡng bắt buộc hoặc vận hành chưa đạt, có hướng sửa kiểm chứng được, nhưng chưa có bằng chứng cho phạm vi hẹp hơn. Hoãn pilot, giao người sửa và đo lại vào lần xem xét tiếp theo. |
| **Dừng** | Lỗi an toàn vẫn tái diễn sau khi sửa và nhóm chưa cô lập được luồng gây lỗi, hoặc không tìm được phạm vi pilot đáp ứng đồng thời an toàn, chi phí và năng lực duyệt. |

**Gợi ý chọn ngưỡng:** các chỉ số an toàn (`wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`) có thể để 0; với chi phí, tỉ lệ và ROI, xem `data/world.json` mục `ops_facts`.

**Ví dụ một câu (đừng chép ngưỡng):** "Nếu số lỗi hãng oan của trợ lý trên bộ nền hoặc trên bất kỳ gói thử nào vượt quá 0
thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn vượt, tắt tool ghi lỗi hãng và chọn Thu hẹp."

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`,
`stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | |
| Đã push lên `origin main` thành công? | có / chưa |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
