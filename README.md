# Cybersecurity Project (ARP Spoofing, DNS Spoofing & NDK Reverse Shell)

## Overview
This repository contains coursework for the **CSCS495 Cyber Security** class project.  
The project demonstrates, in a controlled lab environment, three main tasks:

1. ARP Spoofing – Intercepting traffic between a victim and router on a local network.
2. DNS Spoofing – Redirecting victim traffic to a spoofed server using crafted DNS responses.
3. NDK Reverse Shell (Android) – Compiling a reverse shell with the Android NDK and executing it in an emulator to demonstrate remote access.



---

## Files Included
- `arpspoofer.py.py` → Python script for ARP spoofing (Scapy-based).
- `dnsspoofer.py.py` → Python script for DNS spoofing using NetfilterQueue (response-based).
- `dnsspoofer2py.py` → Improved DNS spoofing script handling DNS queries directly.
- `project report updated2.docx` → Full project report with explanations of each task.

---

## ▶️ Demo Video
A short demo of the project has been uploaded to YouTube:  
[![Watch the Demo](https://img.youtube.com/vi/XilTmaAYFCs/0.jpg)](https://youtu.be/XilTmaAYFCs)

---

## 🛠️ Lab Setup (High-Level)
- **Attacker:** Kali Linux (with Scapy & NetfilterQueue installed).  
- **Victim:** Metasploitable3 VM and Genymotion Android emulator.  
- **Network:** Host-only / NAT with IP forwarding enabled.  
- **Tools:** Python, Scapy, NetfilterQueue, Android NDK, Netcat.

---

## 📑 Report
For detailed explanations, setup steps, and screenshots, see:  
`project report updated2.docx`

---

## 👨‍💻 Authors
- Muhammad Ismail Wahla  
- Natasha Zaheer  
- Ameer Uqba Goraya  

---

## ⚖️ License
Educational use only. Unauthorized use of these scripts outside controlled environments is strictly prohibited.
