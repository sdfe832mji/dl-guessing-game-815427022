answers = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
def hear_guess():
    while True:
        guess = input('A day of the week is....')
        if guess in answers:
            print('Yes!')
            break
        if guess not in answers:
            print('No! Try again...')

print('Can you name a day of the week?')
hear_guess()