apple = {'name':'apple','color':'red'}
strawberry = {'name':'strawberry','color':'green'}
banana = {'name':'banana','color':'blue'}
orange = {'name':'orange','color':'yellow'}
lemon = {'name':'lemon','color':'magenta'}
celery = {'name':'celery','color':'green'}
tomato = {'name':'tomato','color':'blue'}
cherry = {'name':'cherry','color':'red'}

menu = {'apple':apple,'strawberry':strawberry,'banana':banana,'orange':orange,'lemon':lemon,'celery':celery,'tomato':tomato,'cherry':cherry}

sellers = {
    'James':['tomato','apple'],
    'Sarah':['strawberry','banana'],
    'Laura':['tomato','celery']
}

entered_fruit = input('Enter a fruit.').lower()
fruit_info = menu.get(entered_fruit)

if fruit_info is not None:
    print('The fruit is featured!')
    print(fruit_info)

    matching_sellers = []
    for seller, items in sellers.items():
        if entered_fruit in items:
            matching_sellers.append(seller)

    if matching_sellers:
        seller_list = ', '.join(matching_sellers)
        print(f"{entered_fruit.capitalize()} is sold by {seller_list}.")
    else:
        print(f"Nobody sells {entered_fruit}.")

else:
    print('The fruit is not featured in the menu.')