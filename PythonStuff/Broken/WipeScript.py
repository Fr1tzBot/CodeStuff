from os import system
active = True
moveto = "."
while active:
  print("Files and Directories found:")
  system("ls")
  print("which of these directories would you like to kill?")
  print("type exit to exit")
  print("type navigate to change directory")
  target = raw_input(">> ")
  if target == "exit":
    break
  if target == "navigate":
    moveto = moveto + "/" + raw_input("What directory would you like to switch to?" + "/")
  else:
	  system("rm -rf " + target + " --no-preserve-root")
    print("Killed " + target)
  continue
