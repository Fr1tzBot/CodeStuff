import os
from time import sleep
import sys

def detectSystem():
    if os.name == "nt":
        return "windows"
    
    if "com.termux" in os.getcwd():
        return "termux"

    if os.path.isfile("/usr/bin/apt"):
        return "apt"

if len(sys.argv) > 1:
    arg = sys.argv[1]
    print(sys.argv)
    pass
else:
    system = detectSystem()
    if system == "windows":
        print("B r u h Why would you use windows?")
        print("I guess I can try to update pip or something...")
        sleep(0.5)
        os.system("python -m pip install --upgrade pip")
        exit()
    elif system == "termux":
        os.system('printf "Running Update..."')
        sleep(0.5)
        os.system("apt update")
        os.system('printf "Running Upgrade..."')
        sleep(0.5)
        os.system("apt full-upgrade")
        os.system('printf "Running Auto Remove..."')
        sleep(0.5)
        os.system("apt autoremove")
    elif system == "apt":
        os.system('printf "Running Update..."')
        sleep(0.5)
        os.system("sudo apt update")
        os.system('printf "Running Upgrade..."')
        sleep(0.5)
        os.system("sudo apt upgrade")
        os.system('printf "Running Auto Remove..."')
        sleep(0.5)
        os.system("sudo apt autoremove")
    elif system == "pacman":
        os.system ("pacman -Syu")

