updateType=""
#sudo printf "Would you like to preform a full update? [y/n] "
#read updateType
#if [ $updateType == "y" ] || [ $updateType == "Y" ]
    #then
    #echo yeet
#fi
printf "\nRunning Update...\n\n"
sleep 0.5
sudo apt update
printf "\nRunning Upgrade...\n\n"
sleep 0.5
sudo apt upgrade
printf "\nRunning Auto Remove...\n\n"
sleep 0.5
sudo apt autoremove

