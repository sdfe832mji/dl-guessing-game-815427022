while True:
    print('Type \"Easy\" or \"Hard\".')
    chosen_gamemode = input()

    if chosen_gamemode == 'Easy':
        print('Thank you.')
        break
    elif chosen_gamemode == 'Hard':
        print('Well done.')
        break
    else:
        print('Try again please.')
