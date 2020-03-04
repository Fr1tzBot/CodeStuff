#!/bin/bash
clear
passwordPath="/home/fritz/password"
defaultPath="/mnt/Storage/Filez/"
deployTarget=$1
targetIP=""
user="root"
fullLogin=""
port=22
if [[ -f "temp" ]]; then
    rm temp
fi
if [ -z "$deployTarget" ] #check if it is null
    then
    deployTarget=2 #if it is, set to VM mode #TODO: switch to autodetect mode
    echo "Fixed input from null"
    if [ ! $deployTarget -eq $deployTarget ]
        then
        echo "math is broken."
    elif [  $deployTarget -eq 3 ]; 
        then #TODO: create autodetect mode
        echo "This Feature Will Be Added Soon!" #automatically detect which server is active
        #exit 0
    elif [ $deployTarget -eq 2 ]
        then
        targetIP="127.0.0.1" #only the VM is to be targetted
        port=2222
    elif [ $deployTarget -eq 1 ]
        then
        #only the actual server is to be targetted
        targetIP="freenas.local"
    elif [ $deployTarget -eq 0 ]
        #no ssh target is targetted, create a test directory structure on local machine
        #TODO: add this functionality
        then
        echo "No Test Dir Yet!"
        exit 0
    else
        echo "Error: deployTarget Out of Range"
        exit 0
    fi
fi
fullLogin="$user@$targetIP"
if [[ -f "$passwordPath" ]]; then #check if the password file exists
    echo "Beginning SSH Init with User $fullLogin"
    password=$(head -n 1 $passwordPath)
    sshpass -p $password ssh $fullLogin cd "$defaultPath"
    if [ ! $2 -z 1 ]
        then
        echo "updating database..."
        sshpass -p $password ssh $fullLogin /usr/libexec/locate.updatedb > /dev/null 2>&1
    fi
    echo "Done."
else
    echo "Permission Denied: /home/fritz/password not found."
    exit 0
fi
clear
echo "Filename to search for:"
touch temp
read search
echo "$search" > temp
aspell -c temp
search=$(head -n 1 temp)
echo $search
echo "Locate Commands:"
sshpass -p $password ssh $fullLogin locate ${search}
sshpass -p $password ssh $fullLogin locate ${search^}
sshpass -p $password ssh $fullLogin locate ${search^^}
echo "Press Enter When done"
read isDone
rm temp
rm temp.bak