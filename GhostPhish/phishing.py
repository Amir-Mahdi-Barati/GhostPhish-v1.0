import os
import subprocess
import time

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[91m")
    print("╔════════════════════════════════════════════════════════════════════════════╗")
    print("║                            GhostPhish - v1.0                               ║")
    print("╠════════════════════════════════════════════════════════════════════════════╣")
    print("║  Social Engineering Simulation Framework                                   ║")
    print("║  Coded by: Amir Mahdi Barati                                               ║")
    print("║  GitHub: github.com/Amir-Mahdi-Barati                                      ║")
    print("╠════════════════════════════════════════════════════════════════════════════╣")
    print("║  SELECT PHISHING TARGET                                                    ║")
    print("║   [1]  Instagram                                                           ║")
    print("║   [2]  Gmail                                                               ║")
    print("║   [3]  GitHub                                                              ║")
    print("║   [4]  LinkedIn                                                            ║")
    print("║   [5]  Exit                                                                ║")
    print("╚════════════════════════════════════════════════════════════════════════════╝")
    print("\033[0m")
    time.sleep(0.5)

def start_server(target):
    print(f"\033[93m[+] Starting GhostPhish simulation for: {target}\033[0m")
    subprocess.call(['python', 'server.py', target])

if __name__ == "__main__":
    while True:
        banner()
        choice = input("\033[91mGhostPhish > \033[0m")
        targets = {'1': 'instagram', '2': 'gmail', '3': 'github', '4': 'linkedin'}
        if choice in targets:
            start_server(targets[choice])
        elif choice == '5':
            print("\033[91m[!] Exiting GhostPhish... Stay ethical.\033[0m")
            break
        else:
            print("\033[91m[!] Invalid option. Try again.\033[0m")
            time.sleep(1)