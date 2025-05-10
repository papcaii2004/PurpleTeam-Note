# Lateral Movement Techniques  

Repo này tập hợp các kỹ thuật **Lateral Movement** trên các Platform khác nhau.  
- **Mapping theo ATT&CK**: Dễ dàng tra cứu các kỹ thuật theo MITRE ATT&CK.  
- **Lọc theo nền tảng (Windows, Linux, Cloud)**: Tổ chức theo từng hệ điều hành để dễ áp dụng.  
- **Hỗ trợ Adversary Simulation**: Thuận tiện để tìm kiếm và kết hợp các kỹ thuật khi xây dựng mô phỏng tấn công.  

---

## 📌 Repository Structure  

```
├── Windows/
│   ├── Credential-Based/
│   │   ├── PassTheHash/
│   │   ├── PassTheKey/
│   │   ├── PassTheTicket/
│   │   ├── Kerberoasting/
│   ├── Service-Based/
│   │   ├── RemoteServiceExecution/
│   │   ├── ScheduleTasks/
│   │   ├── WMI/
│   │   ├── WinRM/
│   ├── Exploit-Based/
│   ├── README.md
├── Linux/
│   ├── Credential-Based/
│   ├── Service-Based/
│   ├── Exploit-Based/
│   ├── README.md
├── Cloud/
│   ├── AWS/
│   ├── Azure/
│   ├── README.md
├── MITRE.md  <-- Mapping kỹ thuật theo MITRE ATT&CK
├── README.md <-- Tổng quan repo
```

---

## 🔍 Usage
1. **Tìm kỹ thuật theo nền tảng**  
   - Truy cập vào thư mục `Windows/`, `Linux/`, hoặc `Cloud/`.  
   - Chọn nhóm `Credential-Based`, `Service-Based`, hoặc `Exploit-Based`.  
   - Mỗi thư mục có `README.md` với hướng dẫn chi tiết.  

2. **Query theo MITRE ATT&CK**  
   - Xem file [`MITRE.md`](./MITRE.md) để tìm mapping ATT&CK của từng kỹ thuật.  

---

## ✅ TODO
- [ ] Hoàn thiện kỹ thuật `Pass The Hash`, `Pass The Key`, `Kerberoasting`  
- [ ] Bổ sung các kỹ thuật Lateral Movement trên Cloud (AWS, Azure)  
- [ ] Thêm detection & mitigation guide cho từng kỹ thuật  
