# Mythic C2 Framework  
  
## Overview  
  
Mythic is a modern, web-based Command and Control framework written in Python and JavaScript. It provides a collaborative multi-user interface with extensive payload options and advanced operational capabilities for red team engagements.  
  
## Key Features  
  
- **Web-Based Interface**: Browser-accessible collaborative platform  
- **Multi-User Support**: Real-time collaboration with role-based access  
- **Extensive Payload Library**: Cross-platform agents with modular capabilities  
- **RESTful API**: Programmatic access for automation and integration  
- **Docker-Based Deployment**: Containerized architecture for easy deployment  
- **Payload Type System**: Modular agent architecture with custom commands  
  
## Architecture Components  
  
### Core Services  
- **Mythic Server**: Central coordination and web interface  
- **PostgreSQL Database**: Operational data storage  
- **Redis Cache**: Session management and real-time updates  
- **NGINX Proxy**: Load balancing and SSL termination  
- **Payload Type Containers**: Isolated agent compilation environments  
  
## Quick Start  
  
### Installation  
```bash  
# Clone Mythic repository  [header-2](#header-2)
git clone https://github.com/its-a-feature/Mythic  
cd Mythic  
  
# Install and start Mythic  [header-3](#header-3)
sudo ./install_docker_ubuntu.sh  
sudo make  
  
# Access web interface  [header-4](#header-4)
https://127.0.0.1:7443
Initial Configuration
# Create operator account  [header-5](#header-5)
sudo ./mythic-cli mythic_admin create_user  
  
# Install payload types  [header-6](#header-6)
sudo ./mythic-cli install github https://github.com/MythicAgents/apfell  
sudo ./mythic-cli install github https://github.com/MythicAgents/apollo
```

## Basic Workflow

1. Create Operation: Establish operational context
2. Generate Payload: Create agent with specific capabilities
3. Configure Listener: Set up C2 communication channel
4. Deploy Agent: Execute payload on target system
5. Task Management: Issue commands and collect results
  
