import random

required_length = 8
n_lowercase = 2
n_uppercase = 2
n_numbers = 1
n_special = 1

lowercase_characters = 'abcdefghijkmnopqrstuvwxyz' # removed l
uppercase_characters = 'ABCDEFGHJKLMNPQRSTUVWXYZ' # removed I and O
number_characters = '0123456789'
special_characters = '@#$%&*+?!'

lower = random.choices(lowercase_characters, k=n_lowercase)
upper = random.choices(uppercase_characters, k=n_uppercase)
numbers = random.choices(number_characters, k=n_numbers)
special = random.choices(special_characters, k=n_special)
extra = random.choices(lowercase_characters +
                       uppercase_characters +
                       number_characters +
                       special_characters,
                       k = required_length - n_lowercase - n_uppercase - n_numbers - n_special)

all = lower + upper + numbers + special + extra

random.shuffle(all)

password = ''.join(all)

print('New password: ', password)
