#!/usr/bin/env python3
import os
import sys
import subprocess
import platform
import time
import shutil

# --- COLORS & STYLING ---
class Color:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_header():
    clear_screen()
    print(f"{Color.CYAN}{Color.BOLD}")
    print(r"""
  _______ ______ _____  __  __ _____ _   _ _    _  _____ 
 |__   __|  ____|  __ \|  \/  |_   _| \ | | |  | |/ ____|
    | |  | |__  | |__) | \  / | | | |  \| | |  | | (___  
    | |  |  __| |  _  /| |\/| | | | | . ` | |  | |\___ \ 
    | |  | |____| | \ \| |  | |_| |_| |\  | |__| |____) |
    |_|  |______|_|  \_\_|  |_|_____|_| \_|\____/|_____/ 
                                       v1.0.0 | @aaron-devop
    """)
    print(f"{Color.ENDC}")
    print(f"{Color.HEADER}SYSTEM MANAGEMENT INTERFACE for {platform.node()}{Color.ENDC}")
    print(f"{Color.BLUE}{'-'*60}{Color.ENDC}")

# --- FUNCTIONALITY ---

def check_root():
    if os.geteuid() != 0:
        print(f"{Color.FAIL}[!] This tool requires ROOT privileges. Please run with sudo.{Color.ENDC}")
        sys.exit(1)

def run_cmd(command):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return output.decode('utf-8').strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output.decode('utf-8')}"

def service_manager():
    print(f"\n{Color.BOLD}--- [ SERVICE MANAGER ] ---{Color.ENDC}")
    service = input(f"Enter service name (e.g., nginx, mysql): {Color.GREEN}")
    print(f"{Color.ENDC}", end="")
    
    if not service: return

    print("1. Status")
    print("2. Restart")
    print("3. Stop")
    print("4. Start")
    choice = input(f"{Color.CYAN}Action [1-4]: {Color.ENDC}")

    if choice == '1':
        os.system(f"systemctl status {service}")
    elif choice == '2':
        print(f"{Color.WARNING}Restarting {service}...{Color.ENDC}")
        os.system(f"systemctl restart {service}")
    elif choice == '3':
        print(f"{Color.FAIL}Stopping {service}...{Color.ENDC}")
        os.system(f"systemctl stop {service}")
    elif choice == '4':
        print(f"{Color.GREEN}Starting {service}...{Color.ENDC}")
        os.system(f"systemctl start {service}")
    
    input(f"\n{Color.BOLD}Press ENTER to continue...{Color.ENDC}")

def docker_manager():
    print(f"\n{Color.BOLD}--- [ DOCKER COMMANDER ] ---{Color.ENDC}")
    print("1. List Running Containers")
    print("2. List All Containers")
    print("3. View Container Logs")
    print("4. Prune (Clean) System")
    
    choice = input(f"{Color.CYAN}Select [1-4]: {Color.ENDC}")

    if choice == '1':
        os.system("docker ps")
    elif choice == '2':
        os.system("docker ps -a")
    elif choice == '3':
        cid = input("Container ID/Name: ")
        os.system(f"docker logs --tail 50 -f {cid}")
    elif choice == '4':
        print(f"{Color.WARNING}Removing unused data...{Color.ENDC}")
        os.system("docker system prune -f")

    input(f"\n{Color.BOLD}Press ENTER to continue...{Color.ENDC}")

def system_health():
    print(f"\n{Color.BOLD}--- [ QUICK HEALTH CHECK ] ---{Color.ENDC}")
    
    # Load
    load = os.getloadavg()
    print(f"{Color.GREEN}CPU Load (1m, 5m, 15m):{Color.ENDC} {load}")
    
    # Disk
    total, used, free = shutil.disk_usage("/")
    print(f"{Color.GREEN}Disk Usage (/):{Color.ENDC} {int((used/total)*100)}% Used ({free // (2**30)} GB Free)")
    
    # Memory
    mem_cmd = "free -h | grep Mem | awk '{print $3 \" / \" $2}'"
    print(f"{Color.GREEN}Memory Usage:{Color.ENDC} {run_cmd(mem_cmd)}")
    
    # Active Connections
    conns = run_cmd("ss -tuln | grep LISTEN | wc -l")
    print(f"{Color.GREEN}Open Ports:{Color.ENDC} {conns}")

    input(f"\n{Color.BOLD}Press ENTER to continue...{Color.ENDC}")

def network_tools():
    print(f"\n{Color.BOLD}--- [ NETWORK UTILS ] ---{Color.ENDC}")
    print("1. Show Open Ports (Listen)")
    print("2. Show Active Connections")
    print("3. Check Public IP")
    
    choice = input(f"{Color.CYAN}Select [1-3]: {Color.ENDC}")

    if choice == '1':
        os.system("ss -tuln")
    elif choice == '2':
        os.system("netstat -atunp | head -n 20")
    elif choice == '3':
        print(f"Public IP: {run_cmd('curl -s ifconfig.me')}")

    input(f"\n{Color.BOLD}Press ENTER to continue...{Color.ENDC}")

# --- MAIN MENU ---

def main_menu():
    check_root()
    while True:
        print_header()
        print(f"{Color.BOLD}1.{Color.ENDC} Service Manager (Systemd)")
        print(f"{Color.BOLD}2.{Color.ENDC} Docker Commander")
        print(f"{Color.BOLD}3.{Color.ENDC} System Health")
        print(f"{Color.BOLD}4.{Color.ENDC} Network Utilities")
        print(f"{Color.BOLD}5.{Color.ENDC} System Updates (Apt/Yum)")
        print(f"{Color.BOLD}99.{Color.ENDC} Exit")
        
        print(f"{Color.BLUE}{'-'*60}{Color.ENDC}")
        choice = input(f"{Color.CYAN}root@terminus:~# {Color.ENDC}")

        if choice == '1': service_manager()
        elif choice == '2': docker_manager()
        elif choice == '3': system_health()
        elif choice == '4': network_tools()
        elif choice == '5':
            print("Updating system...")
            os.system("apt update && apt upgrade -y" if os.path.exists("/usr/bin/apt") else "yum update -y")
            input("Done. Press ENTER.")
        elif choice == '99':
            print("Terminating session...")
            sys.exit(0)

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nForce Exit.")
