import random # Randomly selects an animal for the game
import time # Spaces out each message for clarity

hints = []

animals = [
    {'name':'Bear', 'skin':'fur', 'diet':'omnivore'},
    {'name':'Piranha', 'skin':'scales','diet':'carnivore'},
    {'name':'Swan', 'skin':'feathers','diet':'herbivore'},
    {'name':'Here','skin':'Here','diet':'Here','size':'Here'}
    ]
# The pool of answers!

def not_option():
    print()
    print('That was not one of the options!')
    print('Try again...')
    time.sleep(2)

def case_reminder():
    print('IMPORTANT:')
    print('This game is input based! All inputs are CASE SENSITIVE!')
    print('To ensure it works, please type with either:')
    print('The first letter capitalized (ex. Hello),')
    print('or the whole word lowercase (ex. hello).')
    print()
    print('If you ever need this message repeated, \n you can type \"HELP\" whenever you can type.')
    time.sleep(5)
# Reminder on how to use inputs.

def restart_game():
    while True:
        print()
        print('Would you like to play again?')
        play_again = input('Please type \"Yes\" or \"No\":')
        if play_again == 'Yes':
            print()
            print('Okay!')
            begin_game()
            break
        elif play_again == 'No':
            print()
            print('See you later! Thank you for playing!')
            break
        else:
            not_option()
# Repeat the game

def start_easy_round():
    print()
    print('The possible answers are:')
    print()
    time.sleep(2)

    answer = random.choice(animals)

    print('Here are your starting hints:')
    print()
    time.sleep(2)

    print('The animal has', answer['skin'], end='')
    print('.')
    print()
    time.sleep(2)

    print('The animal is', answer['diet'], end='')
    print('.')
    print()
    time.sleep(2)

    while True:
        guess_1 = input('What is your first guess? Enter:')

        if guess_1 == answer['name']:
            print()
            print('You got it first try! The answer was', answer['name'], end='')
            print('!')
            time.sleep(2)
            restart_game()
        elif guess_1 not in animals:
            print()
            print('That is not in the answer bank.')
            print('Try again...')
            print()
            time.sleep(2)
        else:
            print()
            print('Not quite. Keep going!')
            print()
            time.sleep(2)

            print('Your next hint is:')
            print('hint here')
# Easy mode round!

def begin_game():
    while True:
        print()
        print('What difficulty would you play on?')
        difficulty = input('Please type \"Easy\" or \"Hard\":')
        if difficulty == 'Easy':
            start_easy_round()
        elif difficulty == 'Hard':
            print('We don\'t have that yet...')
        else:
            not_option()
# Difficulty selection

def greet():
    print('Welcome to my *Animal Guessing Game*!')
    print()
    time.sleep(2)

# Greets new players

#####################################################################################
# THE BEGINNING OF THE GAME # THE BEGINNING OF THE GAME # THE BEGINNING OF THE GAME #
#####################################################################################

greet()
case_reminder()
begin_game()