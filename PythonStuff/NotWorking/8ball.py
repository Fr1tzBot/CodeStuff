import time
import random

ans = True

while ans:
    question = input("Ask the magic 8 ball a question: (press enter to quit) ")
    
    answers = random.randint(1,8)
    
    if question == "":
      print("goodbye")
      break
      
    
    elif answers == 1:
        print "It is certain"
        time.sleep(1)
    
    elif answers == 2:
        print "Outlook good"
        time.sleep(1)
    
    elif answers == 3:
        print "You may rely on it"
        time.sleep(1)
    
    elif answers == 4:
        print "Ask again later"
        time.sleep(1)
    
    elif answers == 5:
        print "Concentrate and ask again"
        time.sleep(1)
    
    elif answers == 6:
        print "Reply hazy, try again"
        time.sleep(1)
    
    elif answers == 7:
        print "My reply is no"
        time.sleep(1)
    
    elif answers == 8:
        print "My sources say no"
        time.sleep(1)

