from os import system

system("git add --all")
commitname = input("Commit Name: ")
print(commitname)
#for error detecting
system("git commit -m " + str(commitname))
system("git push origin CloudShell")
system("git status")

