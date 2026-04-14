# 🔐 SSH Authentication Tester (Brute Force Lab Tool)

<p align="center">
  <img src="https://img.shields.io/badge/Cybersecurity-Offensive%20Security-red?style=flat-square">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python">
  <img src="https://img.shields.io/badge/Focus-Access%20Control%20Testing-orange?style=flat-square">
  <img src="https://img.shields.io/badge/Context-Lab%20Environment-lightgrey?style=flat-square">
</p>

---

## 🎯 Project Objective

This project was developed as part of a **cybersecurity learning initiative** to understand and demonstrate:

- Weak authentication mechanisms
- Risks of poor password policies
- Exposure of SSH services to brute-force attacks
- Defensive considerations (rate limiting, Fail2Ban, key-based auth)

---

## 🧠 Key Skills Demonstrated

- **Offensive Security Basics**
  - Dictionary attacks on SSH services
  - Credential testing methodology

- **Python Development**
  - Multithreading (`ThreadPoolExecutor`)
  - Network interactions using `paramiko`
  - CLI tool design with `argparse`

- **System & Network Understanding**
  - SSH protocol behavior
  - Authentication workflows
  - Handling timeouts and connection failures

- **Secure Coding Practices**
  - Thread-safe execution (`threading.Event`)
  - Error handling (network / authentication exceptions)

---

## ⚙️ Technical Overview

The tool performs a **controlled dictionary attack** against an SSH service:

1. Loads a password wordlist
2. Initiates concurrent authentication attempts
3. Monitors progress in real-time
4. Stops execution immediately upon valid credential discovery

### Core Components:

- `paramiko` → SSH connection handling
- `ThreadPoolExecutor` → Parallel execution
- `threading.Event` → Global stop condition
- Custom progress indicator → Runtime visibility

---

## 🚀 Usage

```bash
python3 brute_forcer.py -t <target_ip> -u <username> -w <wordlist>
