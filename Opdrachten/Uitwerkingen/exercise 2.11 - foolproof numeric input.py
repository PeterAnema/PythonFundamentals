

def foolproof_input(prompt, lower_bound, upper_bound):

    while True:
        try:
            response = input(prompt)
            number = int(response)

            if lower_bound <= number <= upper_bound:
                return number
            else:
                print(f'{number} is not between {lower_bound} and {upper_bound}.')

        except ValueError as ex:
            print(f'"{response}" is not a number.')

        except KeyboardInterrupt:
            print(f'\nOK. Stoping now.')
            break

# ============================================

if __name__ == '__main__':

    number = foolproof_input('Give me a number between 1 and 10: ', 1, 10)

    if number is not None:
        print(f'The number you entered ({number}) is OK')