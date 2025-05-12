# Defense Evasion: AMSI Bypass

## AMSI là gì

### Tổng quan

- `AMSI` **(Antimalware Scan Interface)** là một framework phức tạp được tích hợp vào Windows, cung cấp một interface quét và phân tích dữ liệu nguy hiểm ngay khi dữ liệu đó được tải về hoặc chuẩn bị thực thi (Load vào RAM)

- Nhưng có phải **bất kỳ** đoạn code nào được chạy đều quét qua `AMSI` ?
> Không, amsi là một thư viện nên sẽ chỉ được quét khi một ứng dụng / giải pháp gọi nó
- Một đoạn code sẽ được quét bởi `AMSI` khi chạy từ những platform như:
    - Powershell
    - Windows Script Host (WSH)
    - Microsoft Office macros
    - Windows Defender
    - Hoặc bất kỳ các phần mềm chống virus nào tích hợp `AMSI`

### Cấu trúc lõi

- `AMSI` sử dụng **Component Object Model (COM)** và **RPC**, giúp nó dễ dàng tưởng tác với các ứng dụng và các công cụ AV. Thành phần chính của hệ thống này gồm:
	- `amsi.dll`: Là nhân của hệ thống, bao gồm các functions và API
	- `AmsiScanBuffer` và `AmsiScanString`: Là các functions chính chịu trách nhiệm cho việc scan các mối nguy từ **in-memory** data buffer và strings
	- `IAntimalwareProvider`: Là interface được các AV dùng để tích hợp AMSI vào nó, cho phép các bên thứ ba đóng góp vào threat detection cho AMSI framework

![image](https://learn.microsoft.com/en-us/windows/win32/amsi/images/amsi7archi.jpg)

### Nguyên lý

1. Khi một process Powershell khởi tạo (ở trong bài viết này mình sẽ ví dụ powershell), thư viện `amsi.dll` sẽ được chèn vào không gian bộ nhớ của tiến trình.

2. Sau đó khi một đoạn dữ liệu được tải về hoặc thực thi sẽ được quét thông qua hàm `AmsiScanBuffer`

## Bypass

Sau khi hiểu được nguyên lý thì câu hỏi giờ là làm sao để bypass

### Patch `AmsiScanBuffer`
- Đây là phương pháp đơn giản nhất, vì `amsi.dll` được load vào process nên ta có thể overwrite những byte đầu của function `AmsiScanBuffer` để luôn return TRUE
- Đầu tiên dùng các hàm như `LoadLibrary` và `GetProcAddress` để xác định pointer đến hàm ta cần ghi đè
- Sau đó sử dụng `VirtualProtect` để **đổi quyền truy cập bộ nhớ (đọc ghi)**
- Các phương pháp có thể dùng để ghi là:
    - **`WriteProcessMemory`**: Một API cho phép ghi dữ liệu trực tiếp vào bộ nhớ của tiến trình
    - **`System.Runtime.InteropServices.Marshal.Copy` (trong .NET):** Được dùng để ghi dữ liệu (patch code) vào vùng nhớ đã được cấp quyền ghi, thường thấy trong các bypass AMSI bằng PowerShell hoặc .NET

### Set internal flags
- `amsiInitFailed` là một field nằm trong class `System.Management.Automation.AmsiUtils`
- Khi set thành TRUE tức là set quá trình khởi tạo `AMSI` khi boot không thành công, dẫn đến việc disable framework này 
```powershell
$t=[Ref].Assembly.GetType(('System.Manage'+'ment.Automa'+'tion.AmsiUtils'));
$f=$t.GetField(('amsiIn'+'itFailed'),'NonPublic,Static');
$f.SetValue($null,$true)
```

### RPC Hijack
- Thay vì nhắm vào `amsi.dll`, kỹ thuật này lợi dụng cơ chế **RPC** mà `AMSI` sử dụng


## Resources
- **[Modern APTs and Powershell](https://medium.com/@0xHossam/powershell-exploits-modern-apts-and-their-malicious-scripting-tactics-7f98b0e8090c):** Viết về các aspect khá hay
	- Cách lợi dụng Powershell trong APT
	- **Cơ chế hoạt động của AMSI**
	- Một số phương thức Bypass AMSI
- **[Ghosting-AMSI](https://github.com/andreisss/Ghosting-AMSI):** Kỹ thuật lợi dụng RPC để bypass
