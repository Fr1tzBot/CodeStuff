#echo 'FileDel v1.0 >>>'
#echo 'enter target File extension'
#read FileExtension
#echo 'enter dir path to move to:'
#read TargetPath
#echo 'enter location of files:'
#read FileDir
rm -rf testDir
CreateTestDir () {
    #if [ test -e "~/Documents/CodeStuff/BashStuff/WorkInProgress/testDir/test.txt" ]; then 
        #then
        #file exists
        #echo 'file exists'
    #else
    mkdir testDir
    mkdir testDir/testDir2
    touch testDir/testDir2/test.txt
    touch testDir/testDir2/test2.txt
    echo "created test dir"
    #fi
}
cleanDir () {
    rm -rf testDir
    echo "removed test dir"
}
CreateTestDir
find "testDir/testDir2" -name "*.txt" -type f -exec mv {} "~/Documents/CodeStuff/BashStuff/WorkInProgress/testDir/" \;
#find "~/Documents/CodeStuff/BashStuff/WorkInProgress/testDir/testDir2/"" -name "*.txt" -type f -delete
echo 'remove all .txt files'
