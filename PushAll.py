from os import system

system("git add --all")
commitname = input("Commit Name: ")
print(commitname)
system("git commit -m " + commitname)
system("git push origin CloudShell")
system("git status")
