from flash_cards import *

# Create a dictionary of 15 Spanish or French words and their English
# translations. Call the dict vocab. 
cards = {'un' : 'one', 'deux' : 'two', 'trois' : 'three', 'quatre' : 'four',
         'cinq': 'five', 'six' : 'six', 'sept' : 'seven',  'huit' : 'eight',
         'neuf' : 'nine', 'dix' : 'ten', 'onze' : 'eleven', 'douze' : 'tweleve',
         'treize' : 'thirten', 'quatorze' : 'fourteen'}

correctGoal = 7;

run_game(cards, correctGoal, 'what is the english translation of ', '?')