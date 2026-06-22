Smart Network Intrusion Detection System (NIDS)

A lightweight Network Intrusion Detection System built using Python that captures live network packets, analyzes traffic behavior, and detects suspicious activities like port scanning and unusual access patterns.

🚀 Features
📡 Live network packet sniffing
🧠 Rule-based intrusion detection
⚠️ Suspicious IP detection (anomaly tracking)
🔐 SSH access attempt detection
📝 Logging of security events (CSV format)
💻 Simple CLI-based monitoring system

🧱 Project Structure
NIDS_Project/
│
├── main.py              # Entry point
├── packet_sniffer.py    # Captures live packets
├── detector.py          # Analyzes traffic & detects threats
├── logger.py            # Logs events to CSV
├── dashboard.py         # (Future enhancement - UI)
├── alerts.py            # (Future enhancement - alerts system)
└── logs.csv             # Stores detected events

⚙️ Requirements

Make sure Python is installed:

python --version

Install dependencies:
pip install scapy pandas flask matplotlib


▶️ How to Run
Step 1: Open terminal in project folder
cd NIDS_Project

Step 2: Run the system
python main.py
