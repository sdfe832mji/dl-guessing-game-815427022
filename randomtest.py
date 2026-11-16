import random
import time

cards = ['Red','Orange','Yellow','Green','Blue','Indigo','Violet']

print('I have six cards labelled with the colors of the rainbow (ROYGBIV).')
time.sleep(1)

print('I will draw them in a random order!')
time.sleep(1)

while len(cards) != 0:
    selected_card = random.choice(cards)
    cards.remove(selected_card)
    print(selected_card)
    time.sleep(1)
    continue

print('Do you like the new order?')
time.sleep(1)
print('I think rainbows should look like this instead.')