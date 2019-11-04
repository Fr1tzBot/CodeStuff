from os import system
from time import sleep

system("git status")
sleep(1)
system("git add --all")
sleep(1)
system("git status")
commitname = input("Commit Name: ")
print(commitname)
print(type(commitname))
sleep(1)
#for error detecting
command = "git commit -m '" + str(commitname)
command = command + "'"
print(command)
sleep(1)
system("git config --global user.email 'ftgeib640@pccsk12.com'")
system("git config --global user.name 'Fritz Geib'")
system(command)
system("sudo git push origin master")
system("git status")

