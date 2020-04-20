#password
password = "iamthehacker"
passentry = input("please enter your password: ")
if passentry == password:
  print("Welcome to the Geib Tech Virtual Biusness")
  import time
  time.sleep(5)
  iden = input("please enter your Geib Tech Identification")
  if iden == "thehacker":
    print("Fritz Geib")
  else:
    print("access denied")
else:
  print("access denied")
