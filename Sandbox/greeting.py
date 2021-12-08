

naam = input('Wat is jouw naam? : ')
leeftijd = int(input('Hoe oud ben je? : '))

print('Hallo ' + naam + '. Hoe gaat het? Je bent al ' + str(leeftijd))

print('Hallo %s. Hoe gaat het? Je bent al %d' % (naam, leeftijd))

print('Hallo {}. Hoe gaat het? Je bent al {}'.format(naam, leeftijd))

print(f'Hallo {naam}. Hoe gaat het? Je bent al {leeftijd}')