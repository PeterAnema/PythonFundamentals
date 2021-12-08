

try:
    words = ['a','b','c']

    index = 3
    print(words[index])

    f = open('xxxx')
    number = int(input('Which number? : '))
    result = 100/number
    print(result)

except FileNotFoundError:
    print('That file does not exist!!!')

except ValueError:
    print('This is not a number!!!')

except ZeroDivisionError:
    print('You can not divide by zero!!!')

except Exception as ex:
    print(ex)