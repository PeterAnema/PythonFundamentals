import random

i = 1
totaal = 0
while i <= 5:
    dice = random.randint(1, 6)
    totaal += dice
    print(dice)
    i += 1

# dice1 = random.randint(1, 6)
# dice2 = random.randint(1, 6)
# dice3 = random.randint(1, 6)
# dice4 = random.randint(1, 6)
# dice5 = random.randint(1, 6)

# totaal = dice1 + dice2 + dice3 + dice5 + dice5

# print(dice1, dice2, dice3, dice5, dice5)

print(totaal)