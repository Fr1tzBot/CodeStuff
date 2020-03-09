import time
time.sleep(1)
print("welcome to the python interactived calculator!")
time.sleep(1)
print("This calulator will work as a calculator for dividing, multiplying, subtracting, or adding two numbers.")
time.sleep(1.5)
print("first you will have to enter your first number, then your operator, and finally, your second number.")
time.sleep(1.55)
while True:
  first_number = raw_input("What is your first number?")
  if type(first_number) != "<type 'int'>":
    print("you must enter a number")
    time.sleep(1)
    continue
  operator = input("what is your operator?")
  if operator != "-" or "+" or "/" or "*":
    print("your operator must be either a +,-,/, or *")
    time.sleep(1.8)
    continue
  second_number = raw_input("What is your second number?")
  if type(second_number) != "<type 'int'>":
    print("you must enter a number")
    time.sleep(1)
    continue
  break
if operator == "*" :
  answer = int(first_number) * int(second_number)
  print(answer)
if operator == "/":
  answer = int(first_number) / int(second_number)
  print(answer)
if operator == "+":
    answer = float(first_number) + float(second_number)
    print(answer)
if operator == "-":
    answer = float(first_number) - float(second_number)
    print(answer)
