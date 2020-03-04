#!/bin/bash
passwordPath="/home/fritz/password"
defaultPath="/mnt/Storage/Filez/"
deployTarget=$1
targetIP=""
user="root"
atSign="@"
fullLogin=""
if [ -z "$deployTarget" ] #check if it is null
    then
    deployTarget=2 #if it is, set to VM mode #TODO: switch to autodetect mode
    echo "fixed val from null"
fi
echo $deployTarget
echo $deployTarget==3
if [ $deployTarget==3 ]; then
    echo "This Feature Will Be Added Soon!"
    #automatically detect which server is active
    #TODO: create autodetect mode
elif [ $deployTarget==2 ]
    then
    #only the VM is to be targetted
    targetIP="127.0.0.1:2222"
elif [ $deployTarget==1 ]
    then
    #only the actual server is to be targetted
    targetIP="freenas.local"
elif [ $deployTarget==0 ]
    #no ssh target is targetted, create a test directory structure on local machine
    #TODO: add this functionality
    then
    echo "No Test Dir Yet!"
fi
fullLogin="$user$atSign$targetIP"
echo $fullLogin
echo "Athing, $deployTarget"
if [[ -f "$passwordPath" ]]; then
    echo "Beginning SSH Init..."
    password=$(head -n 1 $passwordPath)
    sshpass -p $password ssh $fullLogin cd "$defaultPath"
    sshpass -p $password ssh $fullLogin sudo /usr/libexec/locate.updatedb
    echo "SSH Init Complete."
else
    echo "Permission Denied: /home/fritz/password not found."
    exit 0
fi
echo "What would you like to search for?"
read search
sshpass -p $password ssh $fullLogin locate $search