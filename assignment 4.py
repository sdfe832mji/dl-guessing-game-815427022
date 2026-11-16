import sys

groceries = []
def add_product(groceries):
    new_product = input('Enter the item to add:')
    groceries.append(new_product)
    print(f'{new_product} has been added to the list.')
    print()
    return groceries
def remove_product(groceries):
    if len(groceries) == 0:
        print('The groceries list is currently empty.')
        return groceries
    else:
        while True:
            new_product = input('Enter the item to remove:')
            if new_product in groceries:
                groceries.remove(new_product)
                print(f'{new_product} has been removed from the list.')
                print()
                return groceries
            else:
                print('The item is not in the list.')
                print('Please try again.')
                print()
                continue
def show_groceries(groceries):
    print('Current Groceries List:')
    for i in range(len(groceries)):
        print(f'{i+1}. {groceries[i]}')
    print()
    return groceries
    print()
def exit_program():
    print('Exiting the program.')
    print()
    sys.exit()
######## Start here
while True:
    print('Grocery List Manager')
    print('1. Add item\n2. Remove item\n3. Show list\n4. Exit')
    choice = input('Enter your choice:')
    if choice == '1':
        groceries = add_product(groceries)
        continue
    elif choice == '2':
        groceries = remove_product(groceries)
        continue
    elif choice == '3':
        groceries = show_groceries(groceries)
        continue
    elif choice == '4':
        exit_program()
        break
    else:
        print('Please enter a number 1-4.')
        print('Please try again.')
        continue
