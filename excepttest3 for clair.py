import random

days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

lives = ['Red','Blue','Green']

selected_day = random.choice(days)

def lost_game():
    print('You lost the game!')

def win_game():
    print('You won the game!')

print()
print()

while True:
    if len(lives) == 1:
        print('You have', len(lives), 'life left.')
    else:
        print('You have', len(lives), 'lives left.')
    print()
    try:
        my_guess = input('Guess what day it is:')

        if len(lives) == 1:
            print()
            print('You ran out of lives!')
            lost_game()
            break
        else:
            selected_life = random.choice(lives)

            if my_guess not in days:
                raise ValueError
            else:
                if my_guess == selected_day:
                    print('You guessed the right day!')
                    win_game()
                    break
                else:
                    print('You guessed the wrong day!')
                    lives.remove(selected_life)
                    print()
                    continue
    except ValueError:
        if my_guess == 'Clair':
            ClairBonus = list()
            lives.extend(ClairBonus)
            continue
        else:
            print()
            print('That is not a valid day!')
            print('Try again!')
            print()
            continue

# TRY NameError