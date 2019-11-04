from os import system
from time import sleep

system("git status")
sleep(5)
system("git add --all")
sleep(5)
system("git status")
commitname = input("Commit Name: ")
print(commitname)
print(type(commitname))
#for error detecting
command = "git commit -m '" + str(commitname)
command = command + "'"
print(command)
system(command)
system("git push origin master")
system("git status")

