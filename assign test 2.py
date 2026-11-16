zebra = {'name':'zebra','diet':'herbivore','skin':'hair','height':'3 to 5 feet tall and 6 to 8 feet long'}
lion = {'name':'lion','diet':'carnivore','skin':'fur','height':'3.5 to 4 feet tall and 6 to 7 feet long.'}
piranha = {'name':'piranha','diet':'carnivore','skin':'scales','height':'5 to 12 inches long'}
flamingo = {'name':'flamingo','diet':'omnivore','skin':'feathers','height':'3 to 5 feet tall'}

zoo = {'zebra':zebra}

entered_animal = input('Enter an animal.')
entered_animal = zoo.get(entered_animal)

if entered_animal is not None:
    print('The animal is featured!')
    print(entered_animal)
    print(entered_animal['height'])
else:
    print('The animal is not featured in the zoo.')