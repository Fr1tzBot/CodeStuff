from pathlib import Path
from shell import exe, reset, runshell
exe("python Concept.py", True)
exit()
print("welcome to Grade manager 1.0")
filecheck = Path("/tmp/GradeManager/.init")
if filecheck.is_file():
  print("Welcome Back!")
  print("Type help for a list of commands")
  while True:
    run = input(">>")
    if run == "help":
      print("help")
      print("exit")
    if run == "exit":
      break
else:
  print("")
  print("Looks like you don't have the needed file installed. Would you like to install them now? (y/n)")
  choice = input(">>")
  if choice == "y":
    #run install script
    exe("mkdir /tmp/GradeManager")
    exe("touch /tmp/GradeManager/.init")
    print("installation complete.")
    print("")
  else:
    print("the program can not run without these scripts, so none of your info will be saved.")
runshell(False)
exe("ls -a /tmp/GradeManager", False)
reset(False)