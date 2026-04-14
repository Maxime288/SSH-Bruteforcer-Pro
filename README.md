# 🔐 SSH Bruteforcer Pro

> **Outil de test de robustesse des identifiants SSH**  
> Un utilitaire performant conçu pour les audits de sécurité et les environnements de laboratoire (CTF).  
> Développé en Python avec une architecture multi-threadée pour une efficacité maximale.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Platform-Kali%20Linux-557C94?logo=kalilinux&logoColor=white">
  <img src="https://img.shields.io/badge/Category-Exploitation-red">
  <img src="https://img.shields.io/badge/Focus-Cybersecurity-orange">
</p>

<p align="center">
  <img src="https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif" width="500">
</p>

---

## 📋 Présentation

**SSH Bruteforcer Pro** est un outil développé dans un cadre **cybersécurité / pentest** visant à démontrer les risques liés à :

- 🔓 Mots de passe faibles
- 🌐 Services SSH exposés
- ⚠️ Absence de protection contre le brute force

---

## 🎯 Objectif du projet

Ce projet met en avant :

- Compréhension des attaques par brute force
- Maîtrise des connexions SSH
- Optimisation des performances (multi-threading)
- Vision offensive ET défensive de la cybersécurité

---

## ⚙️ Installation

```bash
pip install paramiko
git clone https://github.com/Maxime288/SSH-Bruteforcer-Pro.git
cd SSH-Bruteforcer-Pro
chmod +x brute_forcer.py
```

---

## 🚀 Utilisation

```bash
python3 brute_forcer.py -t <IP_CIBLE> -u <UTILISATEUR> -w <WORDLIST>
```

---

## ⚠️ Avertissement Légal

Usage strictement autorisé uniquement (lab, CTF, audit).
