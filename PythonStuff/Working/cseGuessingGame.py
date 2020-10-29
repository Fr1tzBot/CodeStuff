lastAnswer = ""
while True:
    guessesRemaining = 10
    secretNumber = int(input("Player 1 input secret number: "))
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    while True:
        guessesRemaining -= 1
        guess = int(input("\nGuesses Remaining: " + str(guessesRemaining) + "\n" + lastAnswer + "Player 2 Guess The Number: "))
        if guess == secretNumber:
            again = input("Player 2 Wins!\n" + "would you like to play again?")
            break
        elif guess > secretNumber:
            lastAnswer = "You Guessed Too High.\n"
        elif guess < secretNumber:
            lastAnswer = "You Guessed Too Low.\n"
        if guessesRemaining <= 0:
            again = input("Player 1 Wins!\n" + "would you like to play again?")
            break
    if again.lower() in ["y", "yes"]:
        continue
    else:
        break