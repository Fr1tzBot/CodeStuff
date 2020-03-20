#!/bin/bash
clear
#initialize variables
passwordPath="/home/fritz/password"
defaultPath="/mnt/Storage/Filez/"
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
    deployTarget=2 #if it is, set to VM mode #TODO: switch to autodetect mode
    echo "Fixed input from null"
fi
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
    #only a jail in the actual server is to be targetted
    user="fritz"
    targetIP="192.168.66.7"
elif [ $deployTarget -eq 0 ]
    #no ssh target is targetted, create a test directory structure on local machine
    #TODO: add this functionality
    then
    echo "No Test Directory Functionality has been implemented Yet, but I promise it's coming!"
    exit 0
else
    echo "Error: deployTarget Out of Range"
    exit 0
fi
fullLogin="$user@$targetIP" #set the full login
if [[ -f "$passwordPath" ]]; then #check if the password file exists
    echo "Beginning SSH Init..."
    echo "With User $user"
    echo "At host $targetIP"
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
    sshpass -p ${password} ssh -o StrictHostKeyChecking=no ${fullLogin} locate -i ${search} | grep -v "/usr/"
    #sshpass -p ${password} ssh -o StrictHostKeyChecking=no ${fullLogin} "find / -name 'ZX Spectrum'"
    echo "Press Enter When Done."
    read isdone
done

rm temp > /dev/null 2>&1
rm temp.bak > /dev/null 2>&1