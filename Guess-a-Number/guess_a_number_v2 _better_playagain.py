import random
import math
from guessing_game import *

def start_screen():
    title()

def play():

    low = 1
    high = 100
    limit = int(math.log(high-low, 2)) + 1
    tries = 0
    
    print("I'm thinking of a number from " + str(low) + " to " +str(high) + ".")
    print("You try to guess, and I'll tell you if you're right.")
    print("You have " + str(limit) + " attempts to get it.")
    print()

    num = random.randint(1, 100)

    got_it = False

    while got_it == False and tries < limit:
        
        guess = input("What number am I thinking of? ")
        guess = int(guess)
        
        if guess < num:
            print("Nope. Your guess is too low.")
        elif guess > num:
            print("Nope. Your guess is too high.")
        else:
            got_it = True

        tries += 1
        print()

    if got_it == True:
        print("You're a winner!")
    else:
        print("You r dum")

    print()

def play_again():

    while True:
        answer = input("Would you like to play again?")

        if answer == 'no' or answer == 'n':
            return False
        elif answer == 'yes' or answer == 'y':
            return True

        print("what?!!! Just say yes or no, n or y.")


def credit_screen():
    gameOver()
        
#game begins
start_screen()

again = True

while again == True:
    play()
    again = play_again()

credit_screen()