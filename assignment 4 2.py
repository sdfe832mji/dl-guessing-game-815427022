my_awesome_list = []
my_sum = 0

def add_number():
    while True:
        try:
            my_number = int(input('Enter the number: '))
            my_awesome_list.append(my_number)
            print('Added ' + str(my_number) + ' to the list of numbers.')
            return my_awesome_list
        except ValueError:
            print('Please enter a valid number.')
            print('Try again.')
def sum_numbers():
    global my_sum
    if len(my_awesome_list) == 0:
        print('There is no numbers in the list. The sum is 0.')
    else:
        my_sum = sum(my_awesome_list)
        print('The sum is: ' + str(my_sum))
        return my_sum

print('Welcome to my awesome number totaler')
while True:
    print('Would you like to add a number?')
    my_valued_choice = input('Enter \"Add\" to add number.\nIf you are done entering numbers, enter \"Sum\".\n My choice:')
    if my_valued_choice == 'Add':
        add_number()
        continue
    elif my_valued_choice == 'Sum':
        sum_numbers()
        break
    else:
        print('Please follow directions.')
        continue

