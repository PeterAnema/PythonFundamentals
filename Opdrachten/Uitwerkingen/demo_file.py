filename = 'tekst.csv'

with open(filename, 'w') as f:
    f.write('First Name;Last Name; Residense\n')
    f.write('Peter;Anema;Lhee\n')
    f.write('Jeroen;Varenhout;Eindhoven\n')
    print('Bart;Bart;Arnhem', file = f)


with open(filename, encoding='utf8') as f:
    headers = f.readline().rstrip('\n').split(';')

    headers = [header.strip() for header in headers] # remove leading or trailing spaces

    for line in f:
        line = line.rstrip('\n')
        columns = line.split(';')

        columns = [column.strip() for column in columns]  # remove leading or trailing spaces

        d = dict(zip(headers, columns))

        if d['Residense'] == 'Eindhoven':
            print(d['First Name'], d['Last Name'])


