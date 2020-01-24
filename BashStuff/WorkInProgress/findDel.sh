echo 'FileDel v1.0 >>>'
read -p "Target File Extension:" FileExtension
StarDot="*."
FileExtension=$StarDot$FileExtension
#read -p "Path to Copy to:" TargetPath
#echo 'enter location of files:'
#read FileDir
rm -rf testDir
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
cleanDir () {
    cd ~/Documents/CodeStuff/BashStuff/WorkInProgress/
    rm -rf testDir
    rm -rf copyTo
    echo "removed test dir"
}
cleanDir
CreateTestDir
find ~/Documents/CodeStuff/BashStuff/WorkInProgress/testDir/ -name $FileExtension -type f -exec mv {} ~/Documents/CodeStuff/BashStuff/WorkInProgress/copyTo/ \;
find ~/Documents/CodeStuff/BashStuff/WorkInProgress/testDir/ -type d -delete
#find "~/Documents/CodeStuff/BashStuff/WorkInProgress/testDir/testDir2/"" -name "*.txt" -type f -delete
echo 'move all .txt files'
