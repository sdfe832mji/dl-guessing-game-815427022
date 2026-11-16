import random
import time

Zebra = {'name':'Zebra','diet':'herbivore'}
Lion = {'name':'Lion','diet':'carnivore'}
Giraffe = {'name':'Giraffe','diet':'herbivore'}
Panther = {'name':'Panther','diet':'carnivore'}
Flamingo = {'name':'Flamingo','diet':'omnivore'}
Rhino = {'name':'Rhino','diet':'herbivore'}

zoo = [Zebra,Lion,Giraffe,Panther,Flamingo,Rhino]

print('Hello! I have a favorite animal...')
time.sleep(1)

favorite_animal = random.choice(zoo)


print('It\'s a',favorite_animal['name'],end='')
print('!')
time.sleep(1)

print('One thing about it is that it is a',favorite_animal['diet'],end='')
print('.')