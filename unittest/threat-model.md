
## 1. Ai được gọi hàm và để làm gì (Actors)
- admin: quản trị hệ thống. Được xem toàn bộ dữ liệu, kể cả thông tin xác thực.
- operator: vận hành mạng. Cần xem IP quản lý thiết bị để xử lý sự cố.
- viewer: chỉ theo dõi. Chỉ cần xem tóm tắt sự cố (issueSummary).

## 2. Dữ liệu nhạy cảm cần bảo vệ (Assets)
- apiKey: chuỗi SNMP community string, thực chất là mật khẩu truy cập thiết bị. Lộ apiKey thì kẻ tấn công có thể đọc hoặc thay đổi cấu hình thiết bị.
- managementIpAddress: địa chỉ IP quản lý của thiết bị hạ tầng. Lộ IP này giúp kẻ tấn công biết chính xác mục tiêu để dò quét, tấn công.

## 3. Trust boundary bị bỏ qua
- Có một ranh giới giữa người gọi hàm (đã đăng nhập, có role) và dữ liệu thô từ API giám sát. Đáng lẽ dữ liệu phải được lọc theo role trước khi đi qua ranh giới này.
- Bản hiện tại của json_search() không kiểm tra role: ai gọi hàm cũng nhận về toàn bộ giá trị khớp với key. Nghĩa là ranh giới này đang bị bỏ qua hoàn toàn.

## 4. Các mối đe doạ (Threats)
Threat 1 - Information Disclosure (lộ thông tin)
- Một viewer hoặc operator gọi json_search("apiKey", data).
- Hàm trả về chuỗi SNMP community string dù role này không có quyền xem.
- Hậu quả: lộ thông tin xác thực của thiết bị mạng.

Threat 2 - Elevation of Privilege (leo thang đặc quyền)
- Một viewer gọi json_search("managementIpAddress", data) hoặc ("apiKey", data).
- Do hàm không kiểm tra role, viewer nhận được dữ liệu ngang với admin/operator.
- Hậu quả: viewer có quyền đọc vượt quá vai trò được cấp.
