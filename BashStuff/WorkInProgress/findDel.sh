CreateTestDir () {
    #if [ test -e "~/Documents/CodeStuff/BashStuff/WorkInProgress/testDir/test.txt" ]; then 
        #then
        #file exists
        #echo 'file exists'
    #else
    cd ~/Documents/CodeStuff/BashStuff/WorkInProgress/
    mkdir testDir
    mkdir testDir/testDir2
    touch testDir/testDir2/test.txt
    mkdir testDir/testDir3
    touch testDir/testDir3/test2.txt
    mkdir copyTo
    echo "created test dir"
    #fi
}
cleanTestDir () {
    cd ~/Documents/CodeStuff/BashStuff/WorkInProgress/
    rm -rf testDir
    rm -rf copyTo
    echo "removed test dir"
}
echo 'FileDel v1.3 >>>'
read -p "mode?" mode
echo $mode
if [ "$mode" == "test" ]; then
    #run test scripts
    cleanTestDir
    CreateTestDir
    #findFunction ~/Documents/CodeStuff/BashStuff/WorkInProgress/testDir/ "*.txt" f mv ~/Documents/CodeStuff/BashStuff/WorkInProgress/copyTo/
    find ~/Documents/CodeStuff/BashStuff/WorkInProgress/testDir/ -name "*.txt" -type f -exec mv {} ~/Documents/CodeStuff/BashStuff/WorkInProgress/copyTo/ \;
    echo 'move all .txt files'
    #findFunction ~/Documents/CodeStuff/BashStuff/WorkInProgress/testDir/ "" d delete
    find ~/Documents/CodeStuff/BashStuff/WorkInProgress/testDir/ -type d -delete
    echo "delete test dirs"
elif [ "$mode" == "nav"] || [ "$mode" == "navigate"]; then
    cd /
    while [ 1 == 1]
        do
        pwd
        read -p ">>>" moveto
        cd $moveto
        if [ moveto == "exit"]; then
            break
        fi
    done
else
    read -p "Target File Extension: " FileExtension
    StarDot="*."
    FileExtension=$StarDot$FileExtension
    find ~/Documents/CodeStuff/BashStuff/WorkInProgress/testDir/ -name $FileExtension -type f -exec mv {} ~/Documents/CodeStuff/BashStuff/WorkInProgress/copyTo/ \;
    #read -p "Path to Copy to: " TargetPath
    #read -p 'Enter location of files: ' FileDir
fi
#find "~/Documents/CodeStuff/BashStuff/WorkInProgress/testDir/testDir2/"" -name "*.txt" -type f -delete
