"""____Shuffling a deck of card for python beginners____"""

# importing modules
import itertools, random

# make a deck of cards
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

# shuffle the cards with random
random.shuffle(deck)

# draw five cards randomly
print("You ve'got: ")
for i in range(5):
   print(deck[i][0], "of", deck[i][1])