import random

foods = [
    {'name':'Strawberry','color':'red','birth':'seeds'},
    {'name':'Carrot','color':'orange','birth':'no seeds'},
    ]

answer = random.choice(foods) # Pick answer

a = 'The fruit is'+' '+answer['color']+'.'
b = 'The fruit has'+' '+answer['birth']+'.'
hints = [a, b]

def give_hint():
    chosen_hint=(random.choice(hints))
    print(chosen_hint)
    hints.remove(chosen_hint)

print('Your first hint is:')
give_hint()

print()

print('Your second hint is:')
give_hint()

print()

print('The answer was:', answer['name'])