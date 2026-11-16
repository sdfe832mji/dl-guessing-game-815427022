import random

Apple = {'name':'Apple','color':'green'}
Strawberry = {'name':'Strawberry','color':'red'}
Banana = {'name':'Banana','color':'yellow'}
Orange = {'name':'Orange','color':'orange'}

menu = {'apple':Apple,'strawberry':Strawberry,'banana':Banana,'orange':Orange,'berry':Strawberry}

sellers = {
    'James':['strawberry','apple'],
    'Sarah':['strawberry','banana'],
    'Laura':['strawberry','orange']
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