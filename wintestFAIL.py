import random
import time

zebra = {'name':'Zebra','diet':'herbivore','skin':'hair','height':'3 to 5 feet tall and 6 to 8 feet long'}
lion = {'name':'Lion','diet':'carnivore','skin':'fur','height':'3.5 to 4 feet tall and 6 to 7 feet long.'}
piranha = {'name':'Piranha','diet':'carnivore','skin':'scales','height':'5 to 12 inches long'}
flamingo = {'name':'Flamingo','diet':'omnivore','skin':'feathers','height':'3 to 5 feet tall'}

zoo = [zebra,lion,piranha,flamingo]

favorite_animal = random.choice(zoo)

hints = [f'It is a {favorite_animal['diet']}!',
         f'It has {favorite_animal['skin']}!',
         f'On average, it is {favorite_animal["height"]}!',]

print('Hello! I have a favorite animal...')
time.sleep(1)

print('Can you guess what it is?')
time.sleep(1)

while True:
    while len(hints) != 0:

        selected_hint = random.choice(hints)
        hints.remove(selected_hint)
        print(selected_hint)

        my_guess = input('I think the favorite animal is...').lower()

        try:
        if my_guess in zoo:
            if my_guess == favorite_animal['name']:
                print('How did you know!?')
                time.sleep(1)
                break
            elif len(hints) == 1:
                print('That\'s not it...')
                time.sleep(1)
                print('I\'ll give you your LAST hint!')
                time.sleep(1)
            elif len(hints) == 0:
                print('Well, you had enough tries!')
                time.sleep(1)
                print(f'It was the {favorite_animal["name"]}!')
                time.sleep(1)
                break
            else:
                print('That\'s not it...')
                time.sleep(1)
                print('I\'ll give you another hint.')
                time.sleep(1)
                continue
        except ValueError:
                print('That animal is not featured in the zoo.')
                time.sleep(1)
                print('Could you review the answer bank and try again?')
                time.sleep(1)

print(f'Do you like the {favorite_animal["name"]}?')