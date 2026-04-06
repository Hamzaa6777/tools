
Stealth SYN-Scan Detector (Honey-Wall)

A lightweight **Intrusion Detection System (IDS) built with Python and Scapy. This tool monitors network traffic at the **Transport Layer (Layer 4)** to detect unauthorized reconnaissance and "Stealth" SYN scans on high-value database and system ports.


Overview

In a typical production environment, sensitive ports (like **Oracle 1521** or **SSH 22**) should not be probed by unauthorized users. This project acts as a "Honey-Wall," triggering real-time visual alerts the moment a `SYN` packet (the "knock" before a connection) is detected on specified sensitive ports.

 Key Features:
* **Deep Packet Inspection (DPI):** Analyzes raw TCP flags using the Scapy library.
* **Targeted Monitoring:** Specifically watches for the `SYN` flag (Flag 0x02) to catch Nmap stealth scans (`-sS`).
* **High-Value Port Protection:** Pre-configured to monitor common targets like Oracle, MySQL, and SSH.
* **Terminal UI:** Uses ANSI color coding for clear, high-visibility security alerts.


Technical Stack

* **Language:** Python 3.x
* **Core Library:** [Scapy](https://scapy.net/) (Packet Manipulation Tool)
* **Environment:** Linux / macOS (Requires Root/Sudo privileges for raw socket access)

---

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/honey-wall-ids.git
   cd honey-wall-ids
   ```

2. **Install Dependencies:**
   ```bash
   pip install scapy
   ```

3. **Run the Monitor:**
   *Note: You must run with `sudo` to allow Scapy to interface with the network card.*
   ```bash
   sudo python3 honeywall.py
   ```

---

## 🔍 How to Test (PoC)

To simulate an attack and verify the detector, run an **Nmap** scan from another terminal or machine:

```bash
# Perform a stealth SYN scan on the Oracle port
nmap -sS -p 1521 127.0.0.1
```



 Future Roadmap

- [ ] **Automated Mitigation:** Integrate with `iptables` to automatically drop traffic from offending IPs.
- [ ] **Logging:** Export alerts to a `.log` or `.csv` file for SIEM integration.
- [ ] **Multi-Interface Support:** Add a dynamic selector for Wi-Fi, Ethernet, and Loopback interfaces.
- [ ] **Discord/Slack Integration:** Send instant push notifications when a scan is detected.

About the Author

Developed as a security research project by Hamza belghali , an Engineering Student specializing in Cybersecurity. 


