#simple rock paper scissors for sample training
import random
possibles = ("rock", "paper", "scissors")
#1score = 0
#2score = 0
def Run(choice):
  while True:
    p1 = choice
    p1 = p1.lower()
    if not p1 in possibles:
      num1 = possibles[random.randint(0,2)]
    else:
      for i in range(3):
        if possibles[i] == "rock":
          num1 = 1
        if possibles[i] == "paper":
          num1 = 2
        if possibles[i] == "scissors":
          num1 = 3
    num2 = random.randint(1,3)
    if num1 == num2:
      print("Tie!")
      continue
    elif num1 == 1 and num2 == 3:
      print("You Win!")
      break
    elif num1 == 2 and num2 == 1:
      print("You Win!")
      break
    elif num1 == 3 and num2 == 2:
      print("You Win!")
      break
    else:
      print("You Lose!")
      break
  return
