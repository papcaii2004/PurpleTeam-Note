# MITRE ATT&CK Mapping - Discovery  

| Technique ID | Technique Name                     | Sub-Technique                    | OS      | Protocol |
|-------------|-----------------------------------|--------------------------------|--------|----------|
| T1018       | Remote System Discovery           | -                              | Windows, Linux | SMB, ICMP |
| T1082       | System Information Discovery      | -                              | Windows, Linux | API Calls |
| T1046       | Network Service Scanning         | -                              | Windows, Linux | TCP, UDP  |
| T1135       | Network Share Discovery          | -                              | Windows | SMB, RPC |
| T1201       | Password Policy Discovery        | -                              | Windows, Linux | LDAP, Registry |
| T1033       | System Owner/User Discovery      | -                              | Windows, Linux | API Calls |
| T1087       | Account Discovery                | T1087.001 - Local Account Discovery  | Windows, Linux | API Calls |
|             |                                   | T1087.002 - Domain Account Discovery | Windows | LDAP, SAM |
| T1016       | System Network Configuration Discovery | T1016.001 - Internet Connection Discovery | Windows, Linux | API Calls |
|             |                                         | T1016.002 - Network Address Translation Discovery | Windows, Linux | API Calls |
|             |                                         | T1016.003 - Wi-Fi Discovery | Windows, Linux | API Calls |
| T1482       | Domain Trust Discovery           | -                              | Windows | LDAP, RPC |
| T1007       | System Service Discovery         | -                              | Windows | API Calls |
| T1120       | Peripheral Device Discovery      | -                              | Windows | API Calls |
| T1124       | System Time Discovery            | -                              | Windows, Linux | API Calls |

---

## 🔍 Filtering Example
- Nếu cần tìm tất cả kỹ thuật liên quan đến **Windows**, chạy lệnh:
```bash
grep "Windows" MITRE.md
```

- Nếu cần tìm các kỹ thuật dùng LDAP:
```
grep "LDAP" MITRE.md
```

---
