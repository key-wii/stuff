from flash_cards import *

# Create a dictionary of 15 Spanish or French words and their English
# translations. Call the dict vocab. 
cards = {'32' : 'space', '33' : 'exclamation point', '34' : 'double quote',
          '35' : 'number', '36': 'dollar', '37' : 'percent', '38' : 'ampersand',
          '39' : 'single quote', '40' : 'left parenthesis', '41' : 'right parenthesis',
          '42' : 'asterisk', '43' : 'plus', '44' : 'comma', '45' : 'minus',
          '46' : 'period', '47' : 'forward slash', '48' : 'zero', '49' : 'one',
          '50' : 'two', '51' : 'three', '52' : 'four', '53' : 'five', '54' : 'six',
          '55' : 'seven', '56' : 'eight', '57' : 'nine', '58' : 'colon', '59' : 'semicolon',
          '60' : 'less than', '61' : 'equals', '62' : 'greater than', '63' : 'question mark',
          '64' : 'at symbol', '65': 'A', '66' : 'B', '67' : 'C', '68' : 'D', '69' : 'E',
          '70' : 'F', '71' : 'G', '72' : 'H', '73' : 'I', '74' : 'J', '75' : 'K',
          '76' : 'L', '77' : 'M', '78' : 'N', '79' : 'O', '80' : 'P', '81' : 'Q',
          '82' : 'R', '83' : 'S', '84' : 'T', '85' : 'U', '86' : 'V', '87' : 'W',
          '88' : 'X', '89' : 'Y', '90' : 'Z', '91' : 'open bracket', '92' : 'backslash',
          '93' : 'closing bracket', '94' : 'caret', '95' : 'underscore', '96' : 'grave accent',
          '97' : 'a', '98' : 'b', '99' : 'c', '100' : 'd', '101' : 'e', '102' : 'f',
          '103' : 'g', '104' : 'h', '105' : 'i', '106' : 'j', '107' : 'k', '108' : 'l',
          '109' : 'm', '110' : 'n', '111' : 'o', '112' : 'p', '113' : 'q', '114' : 'r',
          '115' : 's'}

correctGoal = 10;

run_game(cards, correctGoal, 'What ascii character does the decimal ', ' represent?')