
# Mythic — Payload Generation

## Payload Type Architecture

Mythic uses a modular payload system: each **Payload Type** runs in its own container and provides its own C2 profiles, build parameters, and implementation details. The Mythic server orchestrates requests and receives artifacts, but the actual build logic lives inside each Payload Type container.

---

## Popular Payload Types

### Sliver

> *Go-based agent supporting multiple C2 protocols*
Reference: [Slithic](https://github.com/papcaii2004/slithic)

**Capabilities**

* Supports mTLS, HTTP(S), WireGuard, DNS, named pipes, etc.
* Can build **session** (interactive) or **beacon** (periodic) implants.
* Output formats: `exe`, `elf`, `shared` (DLL/.so), `shellcode`.

---

### Apfell (macOS / Linux)

> *JavaScript-based agent for POSIX systems*

```text
Payload Type: apfell
C2 Profile: http
Build parameters:
  - callback_host:     192.168.1.100
  - callback_port:     80
  - callback_interval: 10
# Example: build via Mythic UI or the payload container using the parameters above
```

**Capabilities**

* File system operations (read, write, upload, download)
* Process enumeration & management
* Network reconnaissance
* macOS keychain access (where applicable)
* Persistence mechanisms

---

## Build Flow (high level)

1. **User selects options** in the Mythic web UI (payload type, OS, C2 profile, build parameters).
2. **Mythic server** sends an RPC to the corresponding Payload Type container (via RabbitMQ).
3. **Payload container** (e.g., Sliver plugin) reads the parameters, builds the payload (or calls sliver-server via gRPC), and returns artifact bytes or uploads them to Mythic.
4. **Mythic server** stores the artifact and updates UI for download/audit.

---

## Notes & Recommendations

* Always validate and provide correct C2 endpoints (host:port); for mTLS you must ensure certs/keys are available to the payload builder.
* Prefer saved profiles for repeatable builds across engagements.
* Keep build logic inside the Payload Type container — it's easier to maintain and more secure than trying to centralize builds in Mythic core.