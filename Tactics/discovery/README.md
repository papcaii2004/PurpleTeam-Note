# Discovery Techniques  

## 📌 Overview  

**Discovery** là bước kẻ tấn công sử dụng để thu thập thông tin về hệ thống, tài khoản, dịch vụ mạng, cấu hình và các thành phần khác nhằm hỗ trợ cho các bước tiếp theo như **Lateral Movement** hoặc **Privilege Escalation**.  

## 🏛 **Discovery Categories**  

🔹 **AD-Discovery/** → Các kỹ thuật tìm kiếm thông tin trong domain, nhưng có thể chạy từ bất kỳ máy nào trong domain.  
🔹 **DC-Only/** → Chỉ có thể chạy trên Domain Controller hoặc máy có Active Directory module.  
🔹 **Workstation-Discovery/** → Các kỹ thuật trên máy client hoặc standalone.  

---

## 📂 Repository Structure  

```
├── Windows/
│   ├── AD-Discovery/                          
│   │   ├── DomainTrustDiscovery/  
│   │   ├── DomainAccountDiscovery/  
│   │   ├── RemoteSystemDiscovery/ 
│   │   ├── PasswordPolicyDiscovery/ 
│   ├── DC-Only/
│   │   ├── Get-ADUser/                        
│   │   ├── Get-ADComputer/
│   │   ├── Get-ADGroup/
│   │   ├── Get-ADObject/
│   │   ├── Get-DomainPolicy/
│   ├── Workstation-Discovery/
│   │   ├── SystemInformationDiscovery/         
│   │   ├── NetworkServiceScanning/
│   │   ├── NetworkShareDiscovery/
│   │   ├── SystemNetworkConfigurationDiscovery/
│   ├── README.md
├── Linux/
│   ├── System-Discovery/
│   ├── Network-Discovery/
│   ├── Credential-Discovery/
│   ├── README.md
├── MITRE.md
├── README.md
```

---

## 🔍 How to Use  

### 1️⃣ **Tìm kỹ thuật theo môi trường**  
- **Domain-Wide (AD-Discovery)** → Dành cho bất kỳ máy nào trong domain.  
- **Chỉ trên Domain Controller (DC-Only)** → Cần có quyền cao hoặc module AD.  
- **Máy client (Workstation-Discovery)** → Tìm kiếm thông tin trên máy Windows thông thường.  

### 2️⃣ **Query theo MITRE ATT&CK**  
- Xem file [`MITRE.md`](./MITRE.md) để tìm mapping ATT&CK của từng kỹ thuật.  

---
