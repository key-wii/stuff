#Guess-A-Number AI
#
#Jordan Houle
#september 2,2016
import random
import math
from guessing_game import *

def start_screen():
    title()
    print("please enter your name.")
    name = input()

def play():
    
    low = 1
    high = 100
        
    print("Would you like to choose your high and low values?")
    answer = input()

    if answer.lower() == "yes" or answer.lower() == "y":
        print("Low value?")
        low = int(input())
        print("High value?")
        high = int(input())
    elif answer.lower() == "no" or answer.lower() == "n":
        print("okay.")

    else:
        print("What? Okay guess we are going to use the default variables then.")
    
    limit = int(math.log(high-low, 2)) + 1
    tries = 0

    print()

    print("let's play a game that challenges me.")
    print()
    print("You think of a number between " + str(low) + " to " +str(high) + ".")
    print()
    print("I'll try to guess, and you tell me if I'm right.")
    print()
    print("I have " + str(limit) + " attempts to get it.")
    print()
    print("If my guess is to low then put 'higher' or 'h' if my guess is to high then put 'lower'or 'l' and if I get it right type 'yes' or 'y'")
    print()
    print()
    print("Press enter when you have your number.")

    input()

    got_it = False
    
    while got_it == False and tries < limit:
        
        guess = (high + low) //2

        print("Is Your number " + str(guess) + "?")
        answer = input()
        
        if answer.lower() == "yes" or answer.lower() == "y":
            print("yes I got it right!")
            print("I got it in " + str(tries) + " tries.")
            return True
            
        elif answer.lower() == "lower" or answer.lower() == "l":
            high = guess - 1
        elif answer.lower() == "higher" or answer.lower() == "h":
            low = guess + 1

        else:
            print("invalid answer, " + str(name) + ", you are cheating, please follow the rules.")
            tries -=1

        tries += 1
        print()

    if got_it == True:
        print("Yes I' amazing")
        print("I got it in " + str(tries) + ".")
    else:
        print("Wow your good at this game.")

    print()

def play_again():

    while True:
        answer = input("Hey, would you like to play again?")

        if answer.lower() == 'no' or answer.lower() == 'n':
            return False
        elif answer.lower() == 'yes' or answer.lower() == 'y':
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