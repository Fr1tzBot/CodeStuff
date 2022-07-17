def toDec(num: int) -> int:
    output = 0
    for i in range(len(str(num)[::-1])):
        if str(num)[::-1][i] == "1":
            output += 2 ** i
    return output

def toBin(num: int) -> int:
    testNumber = 0
    highestDigit =
    i = 0
    while testNumber < num:
        testNumber = 2 ** i
        i += 1
    testNumber = 2 ** (i-2)
    return testNumber
print(toBin(69))

