import random

easy_animals = []
hard_animals = ['cat', 'dog', 'bird']
cat = {'size':'medium', 'skin':'fur'}
dog = {'size':'large', 'skin':'fur'}
bird = {'size':'small', 'skin':'feathers'}

print('Welcome to the Animal Guessing Game!')

while True:
    print('Would you like to play the Easy or Hard mode?')

    difficulty=input()
    print()

    if difficulty=='Easy' or difficulty=='easy':
        print('*Easy* mode has been selected.')
        break

    elif difficulty=='Hard' or difficulty=='hard':
        print('*Hard* mode has been selected.')
        print('The possible animals are: Dog, Cat, and Bird.')
        answer = random.choice(hard_animals)
        print('An animal from the list has been chosen!')
        print('Your hints are: This is a', (hard_animals.get('size')), 'animal.')
        break

    else:
        print('Please type in either \"Easy\" or \"Hard\" to select your difficulty')