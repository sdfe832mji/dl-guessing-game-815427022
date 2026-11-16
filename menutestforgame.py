import random

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

favorite_item = random.choice(list(menu.keys()))

matching_sellers = []
for seller, items in sellers.items():
    if favorite_item in items:
        matching_sellers.append(seller)

if matching_sellers:
    seller_list = ', '.join(matching_sellers)
    print(f"Sold by {seller_list}.")
else:
    print("No sellers found for this item.")





    ##############
    [f'It is a {item_data['color']}!',
     f'It has {item_data['color']}!',
     f'On average, it is {item_data["color"]}!',