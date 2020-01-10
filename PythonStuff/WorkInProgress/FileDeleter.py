from os import system
active = True
temp = ""
while active:
	print("Please Choose Mode of Deleting:")
	print("[F]Iletype, [D]irectory, or [O]ne file")
	mode = input("")
	modes = ["f", "d", "o"]
	mode = mode.lower()
	if mode not in modes:
		continue
	else:
		if mode == "f":
			#delete filetype mode
			print("what filetype would you like to delete?")
			fType = input("")
			print(range(1, len(fType) - 1))
			if fType[0] == ".":
				for i in range(1, len(fType)):
					temp = temp + fType[i]
				print(temp)
				fType = temp
			print("where is this file located?")
			path = input("")
			if path == "":
				path = "~/Documents/CodeStuff/"
			system("find " + path + " -maxdepth 2 -type f -name  *." + fType + " -delete")
			active = False
			break
		if mode == "d":
			#delete directory
			print("What is the path to your directory?")
			path = input()
			if path[len(path) -1] != "/":
				path = path + "/"
			system("rm -rf " + path)
		if mode == "o":
			#delete one file
			print("What is the Path to the File?")
			path = input()
			system("rm " + path)
		#
	#
#


