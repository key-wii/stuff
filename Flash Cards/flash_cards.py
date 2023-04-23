#Generic file binary and vocab import from

# Add an import statement here so we can use the random.choice function.
import random

def run_game(cards, correct, promptHalf1, promptHalf2):
    # Start the game.
    print("Let's play Flash Cards!")
    right = 0

    # Loop until the player gets the desired amount of consecutive correct answers
    while right < correct:
        # keys from your vocab dict.
        answerKey = list(cards.keys())

        # Use the choice function to select a random word from the
        # list of keys. Store this word in a variable called question.
        question = random.choice(answerKey)

        # Store the corresponding value for that key in a variable
        # called answer.
        answer = cards[question]

        # Print the question word and prompt the user for a guess.
        guess = input(promptHalf1 + question + promptHalf2)
        
        # If guess is equal to answer, print a message stating so and
        # increase the right total by 1. Otherwise, print a message
        # telling the player the correct answer and reset right to zero.
        if guess == answer:
            print('good job!')
            right += 1
        else:
            print('nope')
            right = 0

        # Print the number of consecutive correct answers so far.
        print('you have a streak of ' + str(right) + ' answers.')

    # End the game.
    print("Good job. That's " + str(correct) + " correct answers in a row. You win!")