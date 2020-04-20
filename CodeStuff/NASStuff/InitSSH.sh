#!/bin/bash
#Note: This is one of the few files in the repository that requires a file on my computer
#Note: So if you want to use it, create the file "password" containing your remote password in your home directory
passwordPath="/home/fritz/password"
defaultPath="/mnt/Storage/Filez/"
if [[ -f "$passwordPath" ]]; then
    echo "Beginning SSH Init..."
    password=$(head -n 1 $passwordPath)
    sshpass -p $password ssh root@freenas.local cd "$defaultPath"
    echo "SSH Init Complete."
else
    echo "Permission Denied: /home/fritz/password not found."
fi
