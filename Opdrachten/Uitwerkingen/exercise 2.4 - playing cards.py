import random

# suits = 'clubs diamonds hearts spades'.split()
# or
# suits = ('\u2660', '\u2661', '\u2662', '\u2663')
suits = ('♣', '♢', '♡', '♠')

ranks = '2 3 4 5 6 7 8 9 10 Jack Queen King Ace'.split()
# or
# ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

cards = [f'{r} of {s}' for r in ranks for s in suits]
# or
# cards = [f'{s}{r}' for r in ranks for s in suits]

random.shuffle(cards)
hand = [cards.pop() for _ in range(5)]
# or
# hand = random.sample(cards, k=5)

print(hand)