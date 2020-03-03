#!/bin/bash
passwordPath="/home/fritz/password"
defaultPath="/mnt/Storage/Filez/"
if [[ -f "$passwordPath" ]]; then
    echo "Beginning SSH Init..."
    password=$(head -n 1 $passwordPath)
    sshpass -p $password ssh root@freenas.local cd "$defaultPath"
    sshpass -p $password ssh root@freenas.local sudo /usr/libexec/locate.updatedb
    echo "SSH Init Complete."
else
    echo "Permission Denied: /home/fritz/password not found."
    exit 0
fi
echo "What would you like ot search for?"
read search
sshpass -p $password ssh root@freenas.local locate $search
