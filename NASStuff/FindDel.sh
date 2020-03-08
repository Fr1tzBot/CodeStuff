#!/bin/bash
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
echo 'Modes: "test", '
read -p "mode?" mode
echo $mode
if [ "$mode" == "test" ]; then
    #run test scripts
    cleanTestDir
    CreateTestDir
    find ~/Documents/CodeStuff/BashStuff/WorkInProgress/testDir/ -name "*.txt" -type f -exec mv {} ~/Documents/CodeStuff/BashStuff/WorkInProgress/copyTo/ \;
    echo 'move all .txt files'
    find ~/Documents/CodeStuff/BashStuff/WorkInProgress/testDir/ -type d -delete
    echo "delete test dirs"
else
    read -p "Target File Extension: " FileExtension
    StarDot="*."
    if [ !${FileExtension:0:1}${FileExtension:1:1} == "*."] || [ !${FileExtension:0:1} == "."]; then
        FileExtension=$StarDot$FileExtension
        find ~/Documents/CodeStuff/BashStuff/WorkInProgress/testDir/ -name $FileExtension -type f -exec mv {} ~/Documents/CodeStuff/BashStuff/WorkInProgress/copyTo/ \;
        #read -p "Path to Copy to: " TargetPath
        #read -p 'Enter location of files: ' FileDir
    fi
fi
#find "~/Documents/CodeStuff/BashStuff/WorkInProgress/testDir/testDir2/"" -name "*.txt" -type f -delete
