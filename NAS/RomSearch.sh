#!/bin/bash
#sudo /usr/libexec/locate.updatedb
contains() {
    return [[ $1 =~ (^|[[:space:]])$2($|[[:space:]]) ]] && exit 0 || exit 1 
}
consoleList=("atari 800" "atari 2600" "atari 5200" "atari 7800" "atari jaguar" "atari lynx" "atari st" "atari xegs" "3ds" "ds" "family disk system" "gameboy" "gameboy advance" "gameboy color" "gamecube" "nintendo 64" "nintendo entertainment system" "super nintendo" "wii" "wii u" "final burn alpha" "intellivision" "neo geo" "neo geo pocket" "vectrex" "xbox") 
read -p "What Console is this Game For? " console
#echo "$console" | tr '[:upper:]' '[:lower:]'
declare -l console
console=$console
echo contains $consoleList $console
#if [ contains $consoleList $console ]; then
#    echo "good yeet"
#else
#    echo "bad yeet"
#fi