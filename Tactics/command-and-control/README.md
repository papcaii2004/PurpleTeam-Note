# Command and Control (C2) Frameworks  
  
## Overview  
  
Command and Control frameworks provide the infrastructure for managing compromised systems during red team operations. This documentation covers enterprise-grade C2 deployment strategies, focusing on detection evasion and operational security.  
  
## Framework Comparison  
  
| Framework | Language | Strengths | Use Cases |  
|-----------|----------|-----------|-----------|  
| **Sliver** | Go | Cross-platform, modern protocols, active development | General purpose, enterprise environments |  
| **Mythic** | Python/JavaScript | Web-based interface, extensive payload options | Complex operations, team collaboration |  
| **Cobalt Strike** | Java | Industry standard, extensive documentation | Professional engagements, training |  
  
## Architecture Principles  
  
### Multi-Tier Infrastructure  
Modern C2 operations require layered infrastructure to avoid detection:  
- **Traffic Obfuscation**: Domain fronting and DNS manipulation  
- **Traffic Redirection**: Proxy layers for traffic filtering  
- **Access Control**: Strict firewall rules and source validation  
  
### Framework Selection Criteria  
- **Target Environment**: Operating system compatibility and detection capabilities  
- **Team Size**: Collaboration features and multi-operator support  
- **Operation Duration**: Long-term persistence vs. short-term objectives  
- **Technical Requirements**: Protocol support and payload flexibility  
  
## Documentation Structure  
  
- [`infrastructure/`](./infrastructure/) - Shared infrastructure components  
- [`frameworks/`](./frameworks/) - Framework-specific documentation

## Reference

- [Mastering Modern Red Teaming Infrastructure - Part 2](https://medium.com/@frsfaisall/mastering-modern-red-teaming-infrastructure-part-2-building-stealthy-c2-infrastructure-with-312aec7e1e48)
- MITRE ATT&CK Framework: https://attack.mitre.org/

---