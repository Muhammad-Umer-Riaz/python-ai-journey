# Guess the Number with PyMsgBox
import random
import pymsgbox

secret_number = random.randint(1, 20)

# CHANGED: print() → pymsgbox.alert()
pymsgbox.alert('I am thinking of a number between 1 and 20.')

for guesses_taken in range(1, 7):

    # CHANGED: input() → pymsgbox.prompt(), wrapped in int()
    response = pymsgbox.prompt('Take a guess. (Attempt ' + str(guesses_taken) + ' of 6)')

    # NEW: Handle cancel button or empty input
    if response is None:
        pymsgbox.alert('Game cancelled!')
        break

    guess = int(response)

    if guess < secret_number:
        # CHANGED: print() → pymsgbox.alert()
        pymsgbox.alert('Your guess is too low.')
    elif guess > secret_number:
        # CHANGED: print() → pymsgbox.alert()
        pymsgbox.alert('Your guess is too high.')
    else:
        break  # Correct guess!

if guess == secret_number:
    # CHANGED: print() → pymsgbox.alert()
    pymsgbox.alert('Good job! You got it in ' + str(guesses_taken) + ' guesses!')
else:
    pymsgbox.alert('Nope. The number was ' + str(secret_number))