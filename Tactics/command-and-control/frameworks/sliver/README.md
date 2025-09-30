# Sliver C2 Framework  
  
## Overview  
  
Sliver is a modern, cross-platform Command and Control framework written in Go. It provides robust implant capabilities with support for multiple communication protocols and advanced evasion techniques.  
  
## Key Features  
  
- **Cross-Platform Support**: Windows, Linux, macOS implants  
- **Multiple Protocols**: mTLS, HTTP/HTTPS, DNS, WireGuard  
- **Beacon vs Session Architecture**: Asynchronous and interactive modes  
- **Advanced Evasion**: Process injection, AMSI bypass, ETW evasion  
- **Extensibility**: Custom BOFs and extension support  
  
## Quick Start  
  
### Installation  
```bash  
# Download latest release  [header-9](#header-9)
sudo wget https://github.com/BishopFox/sliver/releases/download/v1.5.42/sliver-server_linux  
mkdir /opt/sliver  
mv sliver-server_linux /opt/sliver/sliver-server_linux  
chmod +x /opt/sliver/sliver-server_linux   
sudo /opt/sliver/sliver-server_linux
```

## Basic Workflow

1. Generate Payload: Create beacon or session implant
2. Start Listener: Configure communication protocol
3. Deploy Payload: Execute on target system
4. Post-Exploitation: Interact with compromised system