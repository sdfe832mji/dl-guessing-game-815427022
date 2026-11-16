import random
hard_animals = ['vanilla', 'chocolate']

def vanilla():
    vanilla = {'flavor': 'sweet', 'genre': 'classic', 'color': 'white'}

def chocolate():
    chocolate = {'flavor': 'sweet', 'genre': 'classic', 'color': 'brown'}

print('The possible answers are:')
print(hard_animals)
print()

answer=(random.choice(hard_animals))
print('A random animal was selected!')
print()
print('This animal is', flavor, 'and', {genre}, end='')
print('.')
print()
