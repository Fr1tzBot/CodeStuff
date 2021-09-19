#!/usr/bin/env python3
import nmap
from pexpect import pxssh
import webbrowser
import socket
import colorama

#Color Functions
def error(message: str) -> None:
    print(colorama.Fore.RED + message + colorama.Style.RESET_ALL)
def warn(message: str) -> None:
    print(colorama.Fore.YELLOW + message + colorama.Style.RESET_ALL)
def success(message: str) -> None:
    print(colorama.Fore.GREEN + message + colorama.Style.RESET_ALL)

def getip() -> str:
    """Return Current IP"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('1.1.1.1', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    success("Local ip: " + ip)
    if ip == "127.0.0.1":
        warn("WARNING: Detected localhost as ip, scan probably won't work")
    return ip

def sshTest(ip: str, username: str, password: str) -> bool:
    """Attempt to login to a given host with given username and password"""
    s = pxssh.pxssh()
    try:
        s.login(ip, username, password)
        s.logout()
        return True
    except pxssh.ExceptionPxssh:
        return False

nm = nmap.PortScanner()
openPorts = {}
sshUsernames = ["root"]
sshPasswords = ["password", "root", "password123"]

#Ports to scan:
#22: SSH
#23: Telnet
#80: HTTP
#443: HTTPS
scanPorts = ["22", "23", "80", "443"]
scanIp = (".".join(getip().split(".")[0:-1])+".0/24")
print("Scanning " + scanIp + " on ports " + ",".join(scanPorts) + "...")
output = nm.scan(scanIp, ",".join(scanPorts), arguments="-T4")

print("scanned " + output["nmap"]["scanstats"]["totalhosts"] + " hosts in " + output["nmap"]["scanstats"]["elapsed"] + " seconds")
print(output["nmap"]["scanstats"]["uphosts"] + " hosts up, " + output["nmap"]["scanstats"]["downhosts"] + " hosts down")
print("\nOpen Ports:")
for i in output["scan"].keys():
    openPorts[i] = []
    for j in output["scan"][i]["tcp"].keys():
        if output["scan"][i]["tcp"][j]["state"] == "open":
            openPorts[i].append(j)
        elif output["scan"][i]["tcp"][j]["state"] == "closed":
            continue
        else:
            warn("WARNING: unrecognized state on " + i + ": " + j)

for i in openPorts:
    for j in range(len(openPorts[i])):
        print("port " + str(openPorts[i][j]) + " on " + str(i))

#Ports to test:
#22: SSH: try a couple of basic logins
#23: Telnet
#80: HTTP: open in a web browser
#443: HTTPS: open in a web browser
print("\nTesting open ports...")
for i in openPorts:
    if 80 in openPorts[i]:
        print("launching http://" + i)
        webbrowser.open("http://" + i)

    if 443 in openPorts[i]:
        print("launching https://" + i)
        webbrowser.open("https://" + i)

for i in openPorts:
    if 23 in openPorts[i]:
        pass

for i in openPorts:
    if 22 in openPorts[i]:
        for j in sshUsernames:
            for k in sshPasswords:
                if sshTest(i, j, k):
                    success(i + ": ssh woked: uname: '" + j + "' passwd: '" + k + "'")
                    break
                else:
                    warn(i + ": ssh failed: uname: '" + j + "' passwd: '" + k + "'")
