import time
time.sleep(1)
print("welcome to the python interactived calculator!")
time.sleep(1)
print("This calulator will work as a calculator for dividing, multiplying, subtracting, or adding two numbers.")
time.sleep(1.5)
print("first you will have to enter your first number, then your operator, and finally, your second number.")
time.sleep(1.55)
first_number = input("What is your first number?")
operator = input("what is your operator?")
second_number = input("What is your second number?")
if operator == "*" :
  answer = int(first_number) * int(second_number)
  print(answer)
if operator == "/":
  answer = int(first_number) / int(second_number)
  print(answer)
if operator == "+":
  try:
    answer = float(first_number) + float(second_number)
    print(answer)
  except ValueError:
    print("you must enter a number")
if operator == "-":
  answer = float(first_number) - float(second_number)
  print(answer)
  time.sleep(1.5)
  quit()


