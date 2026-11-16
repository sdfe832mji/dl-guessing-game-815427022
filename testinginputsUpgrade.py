import random

days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

answer = random.choice(days)

def hear_guess():
    while True:
        guess = input('I think it\'s....')
        if guess in days:
            if guess == answer:
                print('Yeah!')
            else:
                print('No! Today was actually', answer, end='')
                print('!')
            break
        if guess not in days:
            print('No! That\'s not a day! Try again...')


print('Can you guess what day it is today?')
hear_guess()