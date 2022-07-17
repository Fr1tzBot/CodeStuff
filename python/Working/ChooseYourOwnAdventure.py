from time import sleep

answer = ""
answerList = []
hintList = []
yesList = ["y", "yes", "ye", "si", "c", "true", "yep", ]

while True:
    print("Welcome To My Choose Your Own Adventure Game!") #greet the user
    sleep(2)
    input("Press Enter to Start ") 
    print("You wake up an hour late.") #begin the story
    sleep(2)
    print("What do you do, rush to your computer and try to get into class, or just go back to sleep?")
    sleep(1)
    answer = input("(type get to class or back to sleep) ").lower().strip() #take input to decide their option
    sleep(1)
    if answer == "back to sleep": #if they go back to sleep, make sure they can tell that they are a bad person :)
        print("Wow. You are really that lazy?")
        sleep(2)
        print("It's bad enough that you slept past your alarm, and now you're just gonna go back to bed?")
        sleep(2)
        print("I mean seriously, you are just going to spend the entire day in bed because you slept in a bit late?")
        sleep(3)
        print("Well, I guess if that's what you are going to do, I don't really have much of a choice.")
        sleep(3)
        print("Game Over (You asked for it) ")
        answer = input("Play Again? ").lower().strip() #ask if they want to 
        sleep(0.5)
        if answer in yesList:
            continue
        else:
            break
    elif answer == "get to class":
        sleep(1)
        print("You run to your computer to find that your internet is down.")
        sleep(2)
        print("Do you try zoom on your phone, on your laptop, or just give up?")
    else:
        print("You seem to struggle with following directions") #game over error protection
        sleep(3)
        print("choose one of the given choices, or you will die.")
        sleep(3)
        print("Game Over (you died bud) ")
        answer = input("Play Again? ").lower().strip()
        sleep(0.5)
        if answer in yesList:
            continue
        else:
            break
    answer = input("(type phone, laptop, or give up) ").lower().strip() #take input to decide their option
    if answer == "give up":
        sleep(1)
        print("You decide to just go back to sleep.")
        sleep(2)
        print("As you sleep, you spontaneously combust")
        sleep(2)
        print("Game Over (That's what you get for being lazy.) ")
        answer = input("Play Again? ").lower().strip()
        sleep(1)
        if answer in yesList:
            continue
        else:
            break
    elif answer == "laptop": #if user picks laptop
        sleep(2)
        print("The internet doesn't work on your laptop either, so you decide to use your phone.")
    if answer == "laptop" or answer == "phone": #if user picks laptop of phone
        sleep(2)
        print("your phone has a weak connection, so it won't launch zoom.")
        sleep(2)
        print("You run outside of your house, but still don't have a good signal")
        sleep(2)
        print("You think: where can I go?")
        sleep(2)
        print("You realize you could go to a coffee shop, go back and try your laptop again, or try to find a spot with more data")
    else:
        sleep(1)
        print("You seem to struggle with following directions") #game over error protection
        sleep(3)
        print("choose one of the given choices, or you will die.")
        sleep(3)
        print("Game Over (you died bud) ")
        answer = input("Play Again? ").lower().strip()
        sleep(1)
        if answer in yesList:
            continue
        else:
            break
    answer = input("(type coffee, laptop, or data) ").lower().strip() #take input to decide their option
    if answer == "laptop": #if user picks laptop
        sleep(2)
        print(" you open your laptop, and try to log into zoom.")
        sleep(2)
        print("however, due to the stress of existing, your laptop explodes.")
        sleep(2)
        print("Game Over (give your old laptop a break) ")
        answer = input("Play Again? ").lower().strip()
        if answer in yesList:
            continue
        else:
            break
    elif answer == " data": #if user picks data
        sleep(2)
        print("You walk down the street, staring at your phone as you try to load zoom")
        sleep(2)
        print("Suddenly, a huge truck comes speeding down the road.")
        sleep(2)
        print("You try to jump away, but the truck is too fast")
        sleep(2)
        print("Game Over (pay attention when you walk) ")
        answer = input("Play Again? ").lower().strip()
        if answer in yesList:
            continue
        else:
            break
    elif answer == "coffee": #if user picks coffee
        sleep(2)
        print("You begin to walk towards a coffee shop, making sure not to get distracted by your phone.")
        sleep(2)
        print("You walk until you come to a fork in the road.")
        sleep(2)
        print("You can either walk down a the sidewalk, which would take a while, or a dark alley, which is much faster")
    else:
        print("You seem to struggle with following directions") #game over error protection
        sleep(2)
        print("choose one of the given choices, or you will die.")
        sleep(2)
        print("Game Over (you died bud) ")
        answer = input("Play Again? ").lower().strip()
        if answer in yesList:
            continue
        else:
            break
    answer = input("(type alley or sidewalk) ").lower().strip() #take input to decide their option
    if answer == "sidewalk": #if the user picks the sidewalk
        sleep(2)
        print("as you walk down the sidewalk, a sinkhole opens up underneath you")
        sleep(2)
        print("Game Over (I'm running out of ideas) ")
        answer = input("Play Again? ").lower().strip()
        if answer in yesList:
            continue
        else:
            break
    elif answer == "alley": #is the user picks the alley
        sleep(2)
        print("as you walk down the alley, a guy gives you a free phone with unlimited data.")
        sleep(2)
        print("You get to the shop with your new phone, and find that all of your classes are asynchronous today.")
        sleep(2)
        print("Game Over (At least you can use your new phone to explain to your parents why you left the house at 9 am to go to a coffee shop)")
        answer = input("You won, but do you want to Play Again? ").lower().strip()
        if answer in yesList:
            continue
        else:
            break
    else:
        print("You seem to struggle with following directions") #game over error protection
        sleep(2)
        print("choose one of the given choices, or you will die.")
        sleep(2)
        print("Game Over (you died bud) ")
        answer = input("Play Again? ").lower().strip()
        if answer in yesList:
            continue
        else:
            break
    break
print("Thanks For playing my game, Goodbye") #say goodbye
