import msvcrt
import string
import random

for i in range(0, 10):
    randLetter = random.choice(string.ascii_lowercase)
    print("Press " + randLetter + " to cut down the tree")
    while True:
        x = msvcrt.getch()
        if x.decode("utf-8") == randLetter:
            break
        else:
            print("You pressed " + x.decode("utf-8") + " instead of " + randLetter)
            print("Try again")
            continue
    print("You cut down the tree")
    print("You got 1 log")
    print("You got 1 experience point")

print("The tree has fallen")