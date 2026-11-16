import random

book1 = {'name':'Wuthering Heights','length':'600 pages','author':'Emily Bronte'}
book2 = {'name':'Don Quixote','length':'1000 pages','author':'Miguel de Cervantes'}
book3 = {'name':'Demian','length':'200 pages','author':'Herman Hesse'}

favorite_books = [book1,book2,book3]

selected_book = random.choice(favorite_books)
print(selected_book)

if selected_book in favorite_books:
    print('Yes')
elif selected_book not in favorite_books:
    print('No')

