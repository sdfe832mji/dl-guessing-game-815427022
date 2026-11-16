import random

Monday = {'order':'first'}
Tuesday = {'order':'second'}
Wednesday = {'order':'third'}
Thursday = {'order':'fourth'}
Friday = {'order':'fifth'}
Saturday = {'order':'sixth'}
Sunday = {'order':'seventh'}

days = [Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday]

selected_day = random.choice(days)

try:
    my_guess = input('Guess what day it is:')

    position = days.index(my_guess)

    if my_guess == selected_day:
        print('You guessed the right day!')
    else:
        print('You guessed the wrong day!')


except ValueError:
    print('Your guess is not in the list of possible answers.')