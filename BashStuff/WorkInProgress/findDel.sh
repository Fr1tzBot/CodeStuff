echo 'FileDel v1.0 >>>'
echo 'enter target File extension'
#read FileExtension
echo 'enter dir path to move to:'
#read TargetPath
echo 'enter location of files:'
#read FileDir
rm -rf testDir
testDir () {
    pwd
    if [ test -e "~/Documents/CodeStuff/BashStuff/WorkInProgress/testDir/test.txt" ]; then 
        #file exists
        echo 'file exists'
    else
        mkdir testDir
        mkdir testDir/testDir2
        touch testDir/testDir2/test.txt
    fi
}
cleanDir () {
    rm -rf testDir
}
#find FileDir -name $FileExtension -exec mv {} $TargetPath \;
testDir