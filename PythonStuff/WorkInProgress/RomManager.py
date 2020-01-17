from os import system as run

active = True

while active:
    #run
    targetDir = input("Target path? ")
    run('cd ' + targetDir)