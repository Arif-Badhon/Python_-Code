#Game2 Guess the number

import random
import sys

a = random.randint(1,9)

guess = int(input("guess a number between 1 to 9: "))

def compare(a, guess):
    if a == guess:
        return("It is same!")
    elif guess < a:
        return("Too low!!")
    elif guess > a:
        return("Too High!!")
    
    sys.exit()

print(compare(a, guess))

    

