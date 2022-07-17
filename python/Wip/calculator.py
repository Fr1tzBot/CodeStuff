def multisplit(equation: str, characters: str) -> list:
    outlist = [""]
    for i in equation:
        if i in characters:
            outlist.append(i)
            outlist.append("")
        else:
            outlist[-1] += i
    return outlist

def formatEquation(equation: str, symbols: str) -> list:
    equation = multisplit(equation, symbols)
    for i in range(len(equation)):
        if not equation[i] in symbols:
            try:
                equation[i] = float(equation[i])
            except ValueError:
                print("Error: " + equation[i] + " is not a float.")
    return equation

def evaluate(equation: str) -> float:
    """Evaluate an expression into a float"""
    symbols = "+-*/"
    equation = formatEquation(equation, symbols)
    return equation

print(evaluate(input("Enter an equation: ")))