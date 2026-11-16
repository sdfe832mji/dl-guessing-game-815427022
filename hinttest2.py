import random
import time

Zebra = {'name':'Zebra','diet':'herbivore','skin':'hair','height':'3 to 5 feet tall and 6 to 8 feet long'}
Lion = {'name':'Lion','diet':'carnivore','skin':'fur','height':'3.5 to 4 feet tall and 6 to 7 feet long.'}
Piranha = {'name':'Piranha','diet':'carnivore','skin':'scales','height':'5 to 12 inches long'}
Flamingo = {'name':'Flamingo','diet':'omnivore','skin':'feathers','height':'3 to 5 feet tall'}

zoo = [Zebra,Lion,Piranha,Flamingo]

favorite_animal = random.choice(zoo)

hints = [f'It is a {favorite_animal['diet']}!',
         f'It has {favorite_animal['skin']}!',
         f'On average, it is {favorite_animal["height"]}!',]

print('Hello! I have a favorite animal...')
time.sleep(1)

print('It\'s a',favorite_animal['name'],end='')
print('!')
time.sleep(1)

while len(hints) != 0:
    selected_hint = random.choice(hints)
    hints.remove(selected_hint)
    print(selected_hint)
    time.sleep(1)
    continue

print(f'Do you like the {favorite_animal["name"]}?')