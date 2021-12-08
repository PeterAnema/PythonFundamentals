t = input('Give me some text please: ')

print('Original:', t)
print('Upper:', t.upper())
print('Lower:', t.lower())
print('Capitalize:', t.capitalize())
print('Title:', t.title())

print('Ends with a ?', t.endswith('?'))

print('Snake case:', t.lower().replace(' ', '_'))