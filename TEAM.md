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

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

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
