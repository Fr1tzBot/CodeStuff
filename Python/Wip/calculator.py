acceptableOps = "^*/+-"
parsed = [""]
toParse = input("Enter problem:\n> ")
for i in toParse:
    if i in acceptableOps:
        parsed.append("")
        parsed[-1] += i
        parsed.append("")
    else:
        parsed[-1] += i

for i in range(len(parsed)):
    if parsed[i] not in acceptableOps:
        try:
            parsed[i] = float(parsed[i])
        except ValueError:
            print(str(parsed[i]) + " is not a number.\nPlease enter a number.")
            exit()

#couple of checks
if type(parsed[0]) != float:
    print("first character cannot be an operator")
    exit()
if type(parsed[-1]) != float:
    print("last character cannot be an operator")
    exit()

while len(parsed) > 1:
    #an attempt to follow PEMDAS (but without the P cuz that's too much work)
    if "^" in parsed:
        while "^" in parsed:
            index = parsed.index("^")
            parsed[index-1] = parsed[index-1] ** parsed[index+1]
            del parsed[index]
            del parsed[index]
    
    if "*" in parsed:
        while "*" in parsed:
            index = parsed.index("*")
            parsed[index-1] = parsed[index-1] * parsed[index+1]
            del parsed[index]
            del parsed[index]
    
    if "/" in parsed:
        while "/" in parsed:
            index = parsed.index("/")
            parsed[index-1] = parsed[index-1] / parsed[index+1]
            del parsed[index]
            del parsed[index]

    if "+" in parsed:
        while "+" in parsed:
            index = parsed.index("+")
            parsed[index-1] = parsed[index-1] + parsed[index+1]
            del parsed[index]
            del parsed[index]

    if "-" in parsed:
        while "-" in parsed:
            index = parsed.index("-")
            parsed[index-1] = parsed[index-1] - parsed[index+1]
            del parsed[index]
            del parsed[index]

try:
    output = int(parsed[0])
except:
    output = parsed[0]
print(parsed)