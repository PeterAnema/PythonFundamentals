import random

secret_number = random.randint(1, 100)

print('Raad een getal tussen 1 en 100.')

while True:
    gok = int(input('Wat denk je dat het getal is? '))

    if gok == secret_number:
        print('Jaaaaa! Goed geraden!')
        break

    elif gok > secret_number:
        print('lager ...')

    elif gok < secret_number:
        print('hoger ...')