#!/bin/sh
 
### ensure script is run as root/sudo
if ! [ $(id -u) = 0 ]; then
    if [ "$1" ]; then
        echo "Error: root privileges required"
        exit 1
    fi
    sudo sh $0 "1"
    exit $?
fi
 
 
### download and install as root
wget -O /tmp/discord-installer.deb "https://discordapp.com/api/download/canary?platform=linux&format=deb"
dpkg -i /tmp/discord-installer.deb
 
 
### execute discord as real user that invoked script
sudo -u `[ $SUDO_USER ] && echo $SUDO_USER || echo $(whoami)` discord-canary
