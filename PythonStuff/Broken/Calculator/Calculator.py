import math
import time
print("welcome to the python interactived calculator!")
time.sleep(2)
print("This calulator will work as a calculator for dividing, multiplying, subtracting, adding, or exponents with two numbers.")
time.sleep(2)
print("first you will have to enter your first number, then your operator, and finally, your second number.")
time.sleep(2)
print("New in version 6.0! square roots. Type sqrt or square root in the operator menu.")
time.sleep(2)
print("Now with factorials! type a ! in the operator menu!")
time.sleep(3)
while True:
  try:
    first_number = float(input("What is your first number?"))
  except ValueError:
    print("you must enter a number")
    time.sleep(1)
    continue
  operator = input("what is your operator?")
  if operator == "square root" or operator == "sqrt":
    break
  if operator == "!":
    break
  if operator not in "*, /, +, -, ^, !":
    print("your operator must be either a +,-,/, or *")
    time.sleep(1.8)
    continue
  try:
    second_number = float(input("What is your second number?"))
  except ValueError:
    print("you must enter a number")
    time.sleep(1)
    continue
  break
if operator == "*" :
  answer = float(first_number) * float(second_number)
if operator == "/":
  answer = float(first_number) / float(second_number)
if operator == "+":
    answer = float(first_number) + float(second_number)
if operator == "-":
    answer = float(first_number) - float(second_number)
if operator == "square root" or operator == "sqrt":
  answer = math.sqrt(first_number)
if operator == "^":
  answer = (float(first_number) ** float((second_number)))
if operator == "!":
  answer = math.factorial(float(first_number))
print(answer)
