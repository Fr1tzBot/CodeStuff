from os import system
active = True
while active:
	print("Please Choose Mode of Deleting:")
	print("[F]Iletype, [D]irectory, or [O]ne file")
	mode = input("")
	modes = ["f", "d", "o"]
	if mode.lower() not in modes:
		continue
	else:
		

