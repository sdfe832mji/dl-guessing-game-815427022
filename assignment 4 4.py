uppercases = 0
lowercases = 0

mystring = input('Enter your text:')
for character in mystring:
    if character.islower():
        lowercases += 1
    elif character.isupper():
        uppercases += 1
print(f'There are {lowercases} lowercases and {uppercases} uppercases.')

