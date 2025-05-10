# DLL Side-Loading
This is a method that leverage DLL search mechanism of Windows when an application load DLL

Đây là một kỹ thuật lợi dụng cơ chế search order khi load DLL để cài một đoạn mã độc vào trong một ứng dụng hợp lệ

## DLL search order
1. The directory from which the application loaded.
2. Custom search paths (provided by the user).
3. The system directory (e.g., C:\Windows\System32).
4. The Windows directory (e.g., C:\Windows).
5. The current directory.
6. Directories that are listed in the PATH environment variable.

## Cách produce

Để thực hiện DLL side-loading, ta cần:
- Tìm một ứng dụng hợp lệ có lỗi DLL side-loading (search order)
  - Có thể lấy từ các nguồn như [HijackLibs](https://hijacklibs.net/)
- Dựng lên một DLL giả có cấu trúc tương tự DLL gốc
  - Dùng các tool như IDA để xem các Export Function và dựng lại trên DLL giả
  - Các export function giả không nhất thiết phải hoạt động, mà chỉ cần được khai báo
  ![image](https://github.com/user-attachments/assets/64f0714b-177e-48b9-88e1-64e8af3ff186)
  - Sau đó đưa mã độc của ta vào case DLL_PROCESS_ATTACH (được gọi khi DLL được load)
  ![image](https://github.com/user-attachments/assets/87d6c5c0-54d2-42a8-969e-7926ceab6e8e)


- Đóng gói DLL và ứng dụng hợp lệ vào cùng thư mục
- Tạo một file shortcut (LNK) và dùng file LNK này để chạy ứng dụng 

## Cách phát hiện

### Signed PEs load một Unsigned DLL
> Thông thường các PE hợp lệ sẽ được ký, cùng với đó là các DLL kèmm theo. Nếu mà Blue team kiểm tra được PE load một DLL không được ký thì có thể đó là dấu hiệu của một cuộc tấn công

### Loading Path lạ
> Vì DLL side-loading lợi dụng cơ chế search order nên DLL giả sẽ được load trước DLL thật. Ta có thể kiểm tra load path của DLL nếu nó nằm ở các location lạ

## Reference

### POCs/Experience

- **[Red, Blue, Purple Team in DLL Sideloading](https://www.cybereason.com/blog/threat-analysis-report-dll-side-loading-widely-abused):** Worth to read this

#### Red Team
- **[Evading EDR by DLL Sideloading in C#](https://globetech.biz/index.php/2023/05/19/evading-edr-by-dll-sideloading-in-csharp/)**

#### Blue Team

### Known Vulnerable DLLs

- **[Up-to-Date List of Vulnerable DLLs](https://hijacklibs.net/)**
