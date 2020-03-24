#!/bin/bash
clear
#initialize variables
passwordPath="/home/fritz/password"
defaultPath="/"
deployTarget=$1
targetIP=""
user="root"
fullLogin=""
port=22
search="Not Null"
if [[ -f "temp" ]]; then #if the temp file exists, remove it
    rm temp
fi
if [ -z "$deployTarget" ] #check if it is null
    then
    deployTarget=3 #if it is null, automatically detect which server is up
    echo "Mode Defaulted to AutoDetect"
fi
if [ ! $deployTarget -eq $deployTarget ]
    then
    echo "Fatal Error: Math.exe has stopped working."
elif [  $deployTarget -eq 3 ]; 
    then #TODO: create autodetect mode
    if ping -c 1 freenas.local > /dev/null 2>&1
        then
        #real server is up
        deployTarget=1
    else
        #default to vm
        deployTarget=2
    fi
    #automatically detect which server is active
    #exit 0
fi
if [ $deployTarget -eq 2 ]
    then
    targetIP="127.0.0.1" #only the VM is to be targetted
    port=2222
elif [ $deployTarget -eq 1 ]
    then
    #only a jail in the actual server is to be targetted
    user="fritz"
    targetIP="192.168.66.1"
elif [ $deployTarget -eq 0 ]
    #no ssh target is targetted, create a test directory structure on local machine
    #TODO: add this functionality
    then
    echo "No Test Directory Functionality has been implemented Yet, but I promise it's coming!"
    exit 0
elif [ $deployTarget -eq 3 ]
    then
    echo "Error: Autodetect target failed to set a deployTarget"
    exit 0
else
    echo "Error: deployTarget Out of Range (Coded Error)"
    exit 0
fi
fullLogin="$user@$targetIP" #set the full login
if [[ -f "$passwordPath" ]]; then #check if the password file exists
    echo "Beginning SSH Init..."
    echo "Login: $fullLogin"
    password=$(head -n 1 $passwordPath)
    if [ ! $2 -z 1 ]
        then
        echo "Updating Database..."
        sshpass -S -p $password ssh $fullLogin sudo /usr/libexec/locate.updatedb #> /dev/null 2>&1
    fi
    echo "Done."
else
    echo "Permission Denied: /home/fritz/password not found."
    exit 0
fi
touch temp
echo "Press Enter To Launch Search"
read isdone
while [ ! -z "$search" ]
    do
    clear
    echo "Filename to search for: (press enter to exit)"
    read search
    if [ -z "$search" ]
        then
        break
    fi
    echo "$search" > temp
    aspell -c temp
    search=$(head -n 1 temp)
    #echo $search
    echo locate -i ${search}
    #echo $password
    echo "Locate Commands:"
    sshpass -p ${password} ssh ${fullLogin} locate -i ${search} | grep -Ev "/usr/|/var/|/etc/|/lib/|/sbin/|/dev/|/rescue/|/sys/|/bin/|/libexec/|/net/|/root/|/boot/|/home/|/media/|/proc/"
    echo "Press Enter When Done."
    read isdone
done

rm temp > /dev/null 2>&1
rm temp.bak > /dev/null 2>&1