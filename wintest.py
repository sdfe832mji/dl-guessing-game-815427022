import random
import time
import sys

count = 0
winner = False

def start_round():
    global winner
    winner = False

    print('I chose a random day of the week...')
    time.sleep(1)

    days = ['monday','tuesday']

    lives = ['Life']*3

    selected_day = random.choice(days)

    def lost_game():
        print('You lost the game!')

    def win_game():
        global winner
        winner = True
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
            my_guess = input('Guess what day it is:').lower()

            if len(lives) == 0:
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
                        lives.pop(0)
                        print()
                        continue
        except ValueError:
            print()
            print('That is not a valid day!')
            print('Try again!')
            print()
            continue

def loop_game():
    print('Would you like to replay the game?')
    while True:
        replay_consent = input('Please enter \"Yes\" or \"No\".').lower()
        if replay_consent == 'yes':
            print('The game will start shortly.')
            ### Make it start the game again.
            break
        elif replay_consent == 'no':
            print('Thank you for playing!')
            sys.exit(0)
        else:
            print('You entered something other than \"Yes\" or \"No\".')
            time.sleep(1)
            print('Please try again.')
            continue

####################################################### GAME HERE ##################
print('Welcome to the game!')
print('Would you like to play?')

while True:
    game_consent = input('Please enter \"Yes\" or \"No\".').lower()
    if game_consent == 'yes':
        print('The game will start shortly.')
        break
    elif game_consent == 'no':
        print('Thank you for playing!')
        sys.exit(0)
    else:
        print('You entered something other than \"Yes\" or \"No\".')
        time.sleep(1)
        print('Please try again.')
        continue

while True:
    start_round()
    if winner:
        count = count + 1
        if count == 1:
            print('Your current highscore is:')
            print(count,'win.')
        else:
            print('Your current highscore is:')
            print(count,'wins.')
        loop_game()
    else:
        loop_game()
