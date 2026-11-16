import time

zoo = {'Zebra':'name','Lion':'name','Giraffe':'name','Panther':'name','Flamingo':'name','Rhino':'name'}

print('The zoo has a wide variety of animals!')
time.sleep(1)
print('Search to see if the zoo has your favorite animal.')
time.sleep(1)
print('NOTE: Please capitalize the first letter.')
favorite_animal = input('My favorite animal is:')

if favorite_animal in zoo.keys():
    print('Your animal is featured in the zoo!')

else:
    print('Your animal is not featured in the zoo... Sorry!')
    print('Maybe we will introduce this animal in the future.')