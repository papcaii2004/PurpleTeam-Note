# Remote Procedure Call (RPC)

## RPC là gì ?
- **`RPC` (Remote Procedure Call)** là một mô hình kỹ thuật mạng, một giao thức (protocol) nằm ở **session layer** theo OSI model.
### Tại sao lại cần RPC
- Thông thường một process sẽ nằm trong vùng virtual address nó được cấp và chỉ có quyền truy cập memory trong chính process đó
- Nhưng với `RPC`, Nó cho phép một process có thể truy cập một dịch vụ (service) từ **một process khác** (không chỉ trong cùng một máy, mà còn cả từ máy chủ khác, well Remote mà)
### Nguyên lý
- `RPC` sử dụng mô hình **client-server** với các thành phần chính như sau:
	- **Client:** process gửi RPC request
	- **Stubs:** Đóng vai trò trung gian giữa client và server
		- *Client Stub:* 
			- Nằm ở phía client, khởi tạo remote call
			- Chịu trách nghiệm marshalling (serializing) các tham số và unmarshalling (deserializing) kết quả được trả về
		- *Server Stub:* 
			- Nằm ở phía server, tiếp nhận request
			-  Chịu trách nghiệm unmarshalling (deserializing) các tham số và marshalling (serializing) kết quả được trả về
	- **RPC Runtime:** Thư viện xử lý truyền nhận dữ liệu qua mạng
	- **Server:** Process thực thi hàm được request và trả kết quả về client 
![enter image description here](https://images.viblo.asia/ff2487fd-cb95-4507-b104-095bc4993431.png)

## Ứng dụng của RPC
- Windows sử dụng `RPC` cho nhiều dịch vụ hệ thống (DCOM, SMB, Active Directory…)
- Microservices, API Gateway, distributed computing, cloud services