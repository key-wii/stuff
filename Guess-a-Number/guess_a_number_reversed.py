#Guess-A-Number AI
#
#Jordan Houle
#september 1,2016
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

    print()
    print("You think of a number between " + str(low) + " to " +str(high) + ".")
    print("I'll try to guess, and you tell me if I'm right.")
    print("I have " + str(limit) + " attempts to get it.")
    print("If my guess is to low then put 'higher' or 'h' if my guess is to high then put 'lower'or 'l' and if i get it right type 'yes' or 'y'")
    print()
    print("Press enter when you have your number.")
    input()

    got_it = False
    
    while got_it == False and tries < limit:
        
        guess = (high + low) //2

        print("Is Your number " + str(guess) + "?")
        answer = input()
        
        if answer == "yes" or answer == "y":
            print("yes I got it right!")
            return True
            
        elif answer == "lower" or answer == "l":
            high = guess - 1
            
        elif answer == "higher" or answer == "h":
            low = guess + 1
            
        print("What? Input is invalid, you cheater. please input a proper answer.") 
             
        tries += 1
        print()

    if got_it == True:
        print("Yes I' amazing")
    else:
        print("Wow your good at this game.")

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