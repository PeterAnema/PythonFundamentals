filename = 'a_file_that_does_not_exist.txt'

try:
    with open(filename) as f:

        for line in f:
            print(line.rstrip())

except FileNotFoundError:
    print('File "%s\" does not exist' % filename)