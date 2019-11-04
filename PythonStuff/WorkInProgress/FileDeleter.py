from os import system
active = True
while active:
    print("Files and Directories found:")
    system("ls")
    print("which of these directories would you like to kill?")
    print("type exit to exit")
    target = raw_input(">> ")
    if target == "exit":
	break
    else:
	system("rm -rf " + target + " --no-preserve-root")

