#!/bin/bash

if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

# script to check if drive is mounted in /media/fritz/
#mediaDirs="$(find /media/fritz/ -type d | grep -v -e "/media/fritz/")"
#if [ -z "$mediaDirs" ]
#    then
#    echo "not mounted"
#fi

mediaDirs=""
mountName=""
counter=1
dumpPath="/home/fritz/Desktop/floppyDump/"
cd /media/fritz/
mountName="$(find . -type d | grep -v -e ".")"
echo $mountName

if [ ! -d /home/fritz/Desktop/floppyDump ]; then
    mkdir "/home/fritz/Desktop/floppyDump/"
    echo "Created floppyDump Folder."
fi
mountingFunction () {
    if [ ! -e /dev/sdb ]; then
        echo "/dev/sdb Disk Not Detected"
        echo "Attempting to Automount..."
        sudo mount -t vfat /dev/sdb /media/fritz/  > /dev/null 2>&1
        if [ ! -e /dev/sdb ]; then
            echo "Disk still not detected. Aborting."
            exit 0
        fi
        mediaDirs="$(find /media/fritz/ -type d | grep -v -e "/media/fritz/")"
        if [ -z "$mediaDirs" ]
            then
            echo "Automount Failed."
            exit 0
        else
            echo "Automount Success!"
        fi

    else
        echo "Disk Detected"
        echo "Attempting to Automount..."
        sudo mount -t vfat /dev/sdb /media/fritz/ > /dev/null 2>&1
        mediaDirs="$(find /media/fritz/ -type d | grep -v -e "/media/fritz/")"
        if [ ! -z "$mediaDirs" ]
            then
            echo "Automount Failed."
            exit 0
        else
            echo "Automount Success!"
        fi
    fi
}
cd /media/fritz
for i in array {1..$1}
	do
    echo "Please insert disk and press enter when it is inserted"
    read isdone
    mkdir /home/fritz/Desktop/floppyDump/$counter
    dumpPath="/home/fritz/Desktop/floppyDump/$counter"
	sudo mount -t vfat /dev/sdb /media/fritz/ > /dev/null 2>&1
    mountName="$(find . -type d | grep -v -e ".")"
    #cp -v -a "${mediaDirs}." "$dumpPath"
    #find $mediaDirs -exec cp --parents \{\} $dumpPath \;
    find ./$mountName/ -exec cp -v -r \{\} $dumpPath \;
    echo "Copied Files. Please remove disk and press enter"
    sudo umount -t vfat /dev/sdb /media/fritz/ > /dev/null 2>&1
    read isDone
    counter=$(($counter + 1))

done
