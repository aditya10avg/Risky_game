import random
import time
import sys

# Number to guess
number = random.randint(1, 10)
guess = input("Guess a number between 1 and 10: ")
guess = int(guess)

if guess == number:
    print("You guessed correctly!")
else:
    print("You guessed wrong!")
    print("Here's your penalty.")
    print("Simulating deletion of critical macOS system files...\n")


    files = [
        "/System/",
        "/Library/",
        "/bin", "/usr"
    ]

    for file in files:
        sys.stdout.write(f"Deleting {file}...\n")
        sys.stdout.flush()
    

    print("\nSimulation completed.")
