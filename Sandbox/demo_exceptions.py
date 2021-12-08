
def get_number_input(lower, upper):
    while True:
        try:
            number = int(input(f'Give a number between {lower} and {upper}: '))
            if lower <= number <= upper:
                return number
            else:
                print(f'That number is not between {lower} and {upper}!')
        except ValueError:
            print(f'That is not a number!')


def get_number_input(lower, upper):
    while True:
        response = input(f'Give a number between {lower} and {upper}: ')
        if response.isdigit():
            number = int(response)
            if lower <= number <= upper:
                return number
            else:
                print(f'That number is not between {lower} and {upper}!')
        else:
            print(f'That is not a number!')




print( get_number_input(1, 10) )
