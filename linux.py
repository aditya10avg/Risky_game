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
    print("Simulating deletion of critical system files...\n")

   
    files = [
        "/bin", "/etc",
        "/usr", "/var",
    ]
    
    for file in files:
        sys.stdout.write(f"Deleting {file}...\n")
        sys.stdout.flush()
        time.sleep(0.5)  

    print("\nSimulation completed. Sorry for your loss, You need to reinstall Linux OS in your machine now.")
