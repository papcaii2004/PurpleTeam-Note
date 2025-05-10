# MITRE ATT&CK Mapping - Lateral Movement  

| Technique ID | Technique Name                    | Sub-Technique      | OS      | Protocol |
|-------------|----------------------------------|------------------|--------|----------|
| T1550       | Use of Alternate Authentication Material | T1550.002 - Pass The Hash  | Windows | SMB, RPC |
|             |                                  | T1550.003 - Pass The Key   | Windows | RDP      |
|             |                                  | T1550.004 - Pass The Ticket | Windows | Kerberos |
| T1558       | Steal or Forge Kerberos Tickets  | T1558.003 - Kerberoasting  | Windows | Kerberos |
| T1021       | Remote Services                  | T1021.004 - SSH            | Linux   | SSH      |
|             |                                  | T1021.006 - WinRM          | Windows | WinRM    |
|             |                                  | T1021.004 - Remote Service Execution | Windows | SMB, WMI |

---

## 🔍 Filtering Example
- Nếu cần tìm tất cả kỹ thuật liên quan đến **Windows**, chạy lệnh:
```bash
grep "Windows" MITRE.md
```
Nếu cần tìm kỹ thuật dùng **SMB**:
```bash
grep "SMB" MITRE.md
```

