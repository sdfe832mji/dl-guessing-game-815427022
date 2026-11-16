import time

zoo = ['Zebra','Lion','Giraffe','Panther','Flamingo','Rhino']
Zebra = {'diet':'herbivore'}
Lion = {'diet':'carnivore'}
Giraffe = {'diet':'herbivore'}
Panther = {'diet':'carnivore'}
Flamingo = {'Flamingo':'name','diet':'omnivore'}
Rhino = {'diet':'herbivore'}

print('The zoo has a wide variety of animals!')
time.sleep(1)
print('Search to see if the zoo has your favorite animal.')
time.sleep(1)
print('NOTE: Please capitalize the first letter.')
favorite_animal = input('My favorite animal is:')

if favorite_animal in zoo:
    print('Your animal is featured in the zoo!')

else:
    print('Your animal is not featured in the zoo... Sorry!')
    print('Maybe we will introduce this animal in the future.')