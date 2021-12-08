
t = input('Give me some text: ')

print(t)

print(t.upper())
print(t.lower())
print(t.capitalize())
print(t.title())

print(t[:3])

print('Ends with ?', t.endswith('?'))

print('snake case:', t.lower().replace(' ', '_'))
print('kebab case:', t.lower().replace(' ', '-'))


