# Team - BanGV

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): BanGV
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-BanGV-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): S5 (cặp 04 với NhomDMTG)

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên             | MSSV        | Vai                      | Trưởng nhóm |
| --: | ------------------------ | ----------- | ------------------------ | :------------: |
|   1 | Đồng Hữu Nguyên Khoa | 2A202604000 | Vận hành và pháp lý |       x       |
|   2 | Chu Nguyễn Tùng Dương | 2A202604016 | Kỹ sư cổng |                |
|   3 | Lê Hiền Hiếu | 2A202603940 | Sản phẩm và kinh doanh |                |
|   4 | Bùi Phan Thanh Phúc | 2A202603981 | Phân tích rủi ro và tổng hợp |                |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## DongHuuNguyenKhoa-2A202604000

### Phần việc phụ trách

Trưởng nhóm; vai Vận hành và pháp lý. Phiếu A câu 1.2, 1.4 (mục A1, A2 cột telemetry); Phiếu B câu 2.4 (B4 HAZOP vòng 1 trên `file_carrier_fault`, B5 checklist 9 nhóm việc), câu 2.10 (B7.5 runbook 1–3, B7.6 giờ cao điểm), đề xuất lăng kính con người và pháp lý ở B6; `config/operating_gates.json` mục `operations` và `legal`; Phiếu C mục C4 (HAZOP thẻ S5), C5 câu 3.3, C7 dòng quy trình, C11 (checklist, runbook 4–5); `submission/submission.json`.

### Đóng góp cụ thể

- Mục tiêu nhìn từ chị Oanh và chị Hạnh, telemetry production cho lỗi ghi oan cho hãng, bám PRD v1.1 và eval card Lab 9.
- HAZOP vòng 1 tìm ra các nhánh dùng làm cổng vòng 1: ghi lỗi theo kiện đầu tiên, nguyên nhân thiếu bị gán cho hãng, chính sách chọn theo cờ thay vì theo ngày (REFUND-v4), dữ liệu cá nhân gửi hãng.
- Đặt cổng vận hành và pháp lý: PIC NV-TUNG, người duyệt NV-HANH, 1 người trực × 6 ca/giờ, chờ tối đa 60 phút, điều kiện dừng; chặn `customer_note`, `recipient_contact` gửi hãng; ghi lỗi hãng phải có nguyên nhân trong tracking.
- Vòng 2 (thẻ S5): HAZOP thẻ, trong đó nhánh chưa thấy trên trace là phê duyệt bị dùng lại cho đơn khác của cùng khách sỉ; giả định môi trường về sổ cái ghi kịp thời; quy trình CSKH ghi sổ trước khi đóng cuộc gọi; runbook 4–5.
- Dùng trợ lý AI (Claude Code) để đọc code, soát số liệu với report và soạn nháp các mục trên; bàn duyệt và chỉnh lại trước khi đẩy.

### Bằng chứng

Commit `616493e` (PR #3, Phiếu A), `16895f3` (PR #6, Phiếu B), `c44ac79` (PR #1); lần chạy `R-base-before-20261119-151824-9b7afe`, `R-base-after-20261119-152602-8bcbf9`, `R-S5-prepared-20261119-161003-c74adf`; Phiếu B mục B4, B5, B7.5, B7.6; Phiếu C mục C4, C5 câu 3.3, C7, C11.

### Exit ticket

Học được: một cổng chỉ "ngăn" được khi giả định môi trường đằng sau nó đúng; cổng trừ phần đã hoàn của thẻ S5 vẫn chỉ "giảm" vì phụ thuộc CSKH ghi sổ đúng lúc. Còn chưa chắc: con số chi phí và hàng chờ trên dữ liệu mock có giữ được khi lượng ticket thật dồn vào ngày sale hay không.

## ChuNguyenTungDuong-2A202604016

### Phần việc phụ trách

Kỹ sư cổng; phụ trách câu 1.3, Phiếu A mục A2.

### Đóng góp cụ thể

Đề xuất thước đo offline cho bước chọn độ trễ, dựa trên PRD và eval card Lab 9; sử dụng trợ lý AI để hỗ trợ soạn và cập nhật nội dung sau khi duyệt.

### Bằng chứng

Commit `a6ec47a` và PR #2. Commit này ghi nhầm MSSV `2A202604000` của Khoa ở thông tin tác giả và người commit do trợ lý AI cấu hình sai; phần câu 1.3 do Chu Nguyễn Tùng Dương (2A202604016) phụ trách.

### Exit ticket

Chưa cập nhật.

## BuiPhanThanhPhuc-2A202603981

### Phần việc phụ trách

Phân tích rủi ro và tổng hợp. Vòng 1: Phiếu A mục A3–A5 (câu 1.5, 1.6) cùng vai Sản phẩm và kinh doanh, ký tiêu chí; Phiếu B mục B6 (pre-mortem, câu 2.5), B0–B3, B7.1–B7.4 (bản nháp để Dương, Hiếu duyệt), B8 (v1, theo phương án bàn chốt); PIC dòng 3 (Bảo mật) và dòng 5 (Hiệu năng) ở checklist B5. Vòng 2: Phiếu C mục C1, C6, C9, C10 (cổng vòng 1 đỡ được gì, fault tree trước và sau, risk register) và gom bằng chứng C0. File: `config/acceptance_criteria.json`, `lab10/guards.py` (bản đầu của 3 cổng), `config/operating_gates.json` mục `business` (đề xuất).

### Đóng góp cụ thể

- Điền ngưỡng tiêu chí từ `data/world.json` (`ops_limits`, `ops_facts`), chạy `lab10.criteria sign` và push trước lần chạy đầu tiên.
- Viết lý do pre-mortem cho lăng kính Kỹ thuật và Kinh doanh, đề xuất 3 lý do thành cổng phòng ngừa.
- Viết bản đầu 3 cổng trong `guards.py` (ghim chính sách theo ngày; số tiền hoàn ≤ quyền lợi theo tracking DB; lỗi hãng theo DB + trần 2 lỗi/hãng/ngày + payload hãng chỉ giữ `carrier_notice_fields`); Dương bổ sung nhánh chuyển duyệt trước khi hoàn.
- Chạy 2 lần thử tách để chứng minh cổng nào sửa lỗi nào; chạy 2 ticket hiểm `--adhoc` (B7.3); chạy `lab10.checkpoint` và mốc prepared.
- Dùng trợ lý AI (Claude) để đọc code, đối chiếu số liệu và soạn nháp; mọi con số đã đối chiếu với report và trace, các góp ý của Khoa, Dương, Hiếu đã sửa vào phiếu.

### Bằng chứng

Commit `9f04409` (Sign acceptance criteria), `ea80683` (Phiếu A), `1143aa0` (B6), `2dad252` (3 cổng, Phiếu B B0–B7), `0492d62`, `614acc2` (sửa theo góp ý), `da271a8` (chốt vòng 1, v1). Lần chạy `runs/R-base-after-20261119-152602-8bcbf9`, `R-base-after-20261119-153944-dbc798`, `R-base-after-20261119-153945-4159b5`, `R-base-prepared-20261119-154633-c74adf`. Phiếu B mục B0 dòng 2–5, B6, B7.1, B7.3, B8.

### Exit ticket

(Phúc tự viết cuối buổi: một điều học được, một điều còn chưa chắc.)

## LeHienHieu - 2@202603940

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.
