import random

days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

selected_day = random.choice(days)

class NotInTheAnswers(Exception):
    'Raised when the input value is not in the list of possible answers.'
    pass
try:
    my_guess = input('Guess what day it is:')

    if my_guess not in days:
        raise NotInTheAnswers
    else:
        if my_guess == selected_day:
            print('You guessed the right day!')
        else:
            print('You guessed the wrong day!')
except NotInTheAnswers:
    print('Your guess is not in the list of possible answers.')

# TRY NameError