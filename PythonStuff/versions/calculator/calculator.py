import time
time.sleep(1)
print("welcome to the python interactived calculator!")
time.sleep(1)
print("This calulator will work as a calculator for dividing, multiplying, subtracting, or adding two numbers.")
time.sleep(1)
print("first you will have to enter your first number, then your operator, and finally, your second number.")
time.sleep(1)
first_number = input("What is your first number?")
time.sleep(1)
if type(first_number) != "<type 'int'>" or type(second_number) != "<type 'int'>":
  print("you must enter a number")
  time.sleep(1)
  quit()
operator = input("what is your operator?")
time.sleep(1)
second_number = input("What is your second number?")
if type(first_number) != "<type 'int'>" or type(second_number) != "<type 'int'>":
  print("you must enter a number")
  time.sleep(1)
  quit()
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
