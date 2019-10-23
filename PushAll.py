from os import system

system("git add --all")
commitname = input("Commit Name: ")
print(commitname)
print(type(commitname))
#for error detecting
command = "git commit -m '" + str(commitname)
command = command + "'"
print(command)
system(command)
system("git push origin CloudShell")
system("git status")

