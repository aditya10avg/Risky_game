import random
import time
import sys

number = random.randint(1, 10)
guess = input("Guess a number between 1 and 10: ")
guess = int(guess)

if guess == number:
    print("You guessed correctly!")
else:
    print("You guessed wrong!")
    print("Here's your penalty.")
    print("Deleting Windows System32...\n")

    # Simulate file deletion with loading dots
    for i in range(30):
        sys.stdout.write("\rDeleting file: System32\\file" + str(i) + ".dll")
        sys.stdout.flush()
        time.sleep(0.1)

    print("\nSystem32 deletion completed! (just kidding, no files were harmed) but don't try windows.py at any chance, it's dangerous and doesn't jokes.")
