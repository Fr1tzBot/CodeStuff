import math
import time
time.sleep(1)
print("welcome to the python interactived calculator!")
time.sleep(1)
print("This calulator will work as a calculator for dividing, multiplying, subtracting, adding, or exponents with two numbers.")
time.sleep(1.5)
print("first you will have to enter your first number, then your operator, and finally, your second number.")
time.sleep(1.55)
print("New in version 6.0! square roots. Type squrt or square root in the operator menu.")
time.sleep(1.555)
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
  if operator not in "*, /, +, -, ^":
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
print(answer)  
