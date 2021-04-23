from datetime import datetime
import string
import itertools
password = input("what password would you like to crack? ")
startTime = datetime.now()
characters = " abcdefghijklmnopqrstuvwxyz1234567890"
guess = ""

def guess_password(real):
    global characters
    attempts = 0
    for password_length in range(1, 9):
        for guess in itertools.product(characters, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            if guess == real:
                return 'password is {}. found in {} guesses.'.format(guess, attempts)
            print(guess, attempts)

#while guess != password:
#    for i in range(len(characters)):
print(guess_password(password))


print("Time: " + str(datetime.now() - startTime))