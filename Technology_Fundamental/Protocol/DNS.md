# Giao thức DNS

## 1. Tổng quan về DNS

### 1.1 Khái niệm cơ bản
- DNS (Domain Name System) là hệ thống phân cấp và phân tán để đặt tên
- Chức năng chính: Chuyển đổi tên miền dễ đọc sang địa chỉ IP
- Hoạt động như một cơ sở dữ liệu phân tán
- Sử dụng mô hình client-server với kiến trúc phân cấp

### 1.2 Đặc điểm giao thức
- **Giao thức truyền tải**:
  - UDP cổng 53: Chủ yếu dùng cho truy vấn
  - TCP cổng 53: Dùng cho chuyển vùng và phản hồi > 512 bytes
- **Kích thước gói tin**:
  - Gói tin DNS qua UDP: Giới hạn 512 bytes
  - Gói tin DNS qua TCP: Tối đa 65,535 bytes
- **EDNS0**: Cơ chế mở rộng cho DNS để hỗ trợ gói tin UDP lớn hơn

## 2. Cấu trúc phân cấp DNS

### 2.1 Cấu trúc không gian tên miền
```
                     . (Root - Gốc)
                     /     |      \
                    /      |       \
                .com    .org     .net
                /         |         \
            example    google      site
            /            |          \
        www           mail        blog
```

### 2.2 Các cấp tên miền
1. Tên miền gốc (Root Domain - .)
2. Tên miền cấp cao nhất (TLD)
3. Tên miền cấp hai
4. Tên miền phụ

## 3. Các bản ghi DNS

### 3.1 Các loại bản ghi phổ biến
- **Bản ghi A**: Ánh xạ địa chỉ IPv4
  - Định dạng: `tên-miền IN A địa-chỉ-IPv4`
  - Ví dụ: `example.com. IN A 93.184.216.34`

- **Bản ghi AAAA**: Ánh xạ địa chỉ IPv6
  - Định dạng: `tên-miền IN AAAA địa-chỉ-IPv6`
  - Ví dụ: `example.com. IN AAAA 2606:2800:220:1:248:1893:25c8:1946`

- **Bản ghi CNAME**: Tên miền phụ (bí danh)
  - Định dạng: `bí-danh IN CNAME tên-gốc`
  - Ví dụ: `www.example.com. IN CNAME example.com.`

- **Bản ghi MX**: Máy chủ thư điện tử
  - Định dạng: `tên-miền IN MX độ-ưu-tiên máy-chủ-mail`
  - Ví dụ: `example.com. IN MX 10 mail.example.com.`

- **Bản ghi NS**: Máy chủ tên miền
  - Định dạng: `tên-miền IN NS nameserver`
  - Ví dụ: `example.com. IN NS ns1.example.com.`

- **Bản ghi PTR**: Phân giải ngược DNS
  - Định dạng: `IP-ngược IN PTR tên-miền`
  - Ví dụ: `34.216.184.93.in-addr.arpa. IN PTR example.com.`

- **Bản ghi SOA**: Khởi đầu ủy quyền
  - Định dạng: `tên-miền IN SOA ns-chính email-admin (số-sê-ri làm-mới thử-lại hết-hạn tối-thiểu)`
  - Ví dụ: 
    ```
    example.com. IN SOA ns1.example.com. admin.example.com. (
        2023100101  ; Số sê-ri
        3600        ; Thời gian làm mới (1 giờ)
        1800        ; Thời gian thử lại (30 phút)
        604800      ; Thời gian hết hạn (1 tuần)
        86400       ; TTL tối thiểu (1 ngày)
    )
    ```

## 4. Quy trình phân giải DNS

### 4.1 Các loại truy vấn
1. **Truy vấn đệ quy (Recursive Query)**
   - Client → Resolver đệ quy
   - Resolver xử lý toàn bộ quá trình phân giải
   - Trả về kết quả cuối cùng cho client

2. **Truy vấn tương tác (Iterative Query)**
   - Server → Các máy chủ có thẩm quyền
   - Mỗi server chỉ dẫn đến server tiếp theo trong hệ thống phân cấp
   - Tiếp tục cho đến khi tìm được câu trả lời có thẩm quyền

### 4.2 Các bước phân giải
1. Client gửi truy vấn đến resolver đệ quy
2. Resolver truy vấn máy chủ root
3. Máy chủ root chỉ dẫn đến máy chủ TLD
4. Máy chủ TLD chỉ dẫn đến máy chủ có thẩm quyền
5. Máy chủ có thẩm quyền cung cấp câu trả lời cuối cùng
6. Resolver trả kết quả về cho client

### 4.3 Định dạng gói tin DNS
```
+------------------+
|      Header     |
+------------------+
|     Câu hỏi     |
+------------------+
|     Trả lời     |
+------------------+
|   Thẩm quyền    |
+------------------+
|     Bổ sung     |
+------------------+
```

#### Các trường trong Header
- ID (16 bits)
- Cờ (16 bits)
  - QR: Truy vấn/Phản hồi
  - OPCODE: Mã hoạt động
  - AA: Trả lời có thẩm quyền
  - TC: Cắt ngắn
  - RD: Yêu cầu đệ quy
  - RA: Hỗ trợ đệ quy
  - Z: Dự phòng
  - RCODE: Mã phản hồi
- QDCOUNT: Số lượng câu hỏi
- ANCOUNT: Số lượng câu trả lời
- NSCOUNT: Số lượng bản ghi thẩm quyền
- ARCOUNT: Số lượng bản ghi bổ sung

## 5. Bộ nhớ đệm DNS

### 5.1 Các cấp độ bộ nhớ đệm
1. **Bộ nhớ đệm trình duyệt**
   - TTL ngắn nhất
   - Lưu trữ riêng cho từng trình duyệt

2. **Bộ nhớ đệm hệ điều hành**
   - Bộ nhớ đệm toàn hệ thống
   - Quản lý bởi resolver của hệ điều hành

3. **Bộ nhớ đệm resolver**
   - Bộ nhớ đệm của ISP hoặc nhà cung cấp DNS
   - Dùng chung cho nhiều người dùng

### 5.2 TTL (Thời gian tồn tại)
- Xác định thời gian bản ghi được lưu trong bộ nhớ đệm
- Được thiết lập bởi quản trị viên vùng
- Giá trị thông thường:
  - TTL ngắn: 300-900 giây
  - TTL chuẩn: 3600-86400 giây
  - TTL dài: > 86400 giây

## Tham khảo
- RFC 1034 - Tên miền - Khái niệm và Cơ sở
- RFC 1035 - Tên miền - Triển khai và Đặc tả
- RFC 2535 - Phần mở rộng bảo mật DNS
- RFC 3596 - Phần mở rộng DNS để hỗ trợ IPv6
