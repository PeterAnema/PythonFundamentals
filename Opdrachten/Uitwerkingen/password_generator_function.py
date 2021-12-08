import random

def generate_password(required_length = 8,
                      n_lowercase = None,
                      n_uppercase = None,
                      n_numbers = None,
                      n_special = None):

    lowercase_characters = 'abcdefghijkmnopqrstuvwxyz'  # removed l
    uppercase_characters = 'ABCDEFGHJKLMNPQRSTUVWXYZ'  # removed I and O
    number_characters = '0123456789'
    special_characters = '@#$%&*+?!'

    lower = random.choices(lowercase_characters, k=n_lowercase if n_lowercase is not None else 1)
    upper = random.choices(uppercase_characters, k=n_uppercase if n_uppercase is not None else 1)
    numbers = random.choices(number_characters, k=n_numbers if n_numbers is not None else 1)
    special = random.choices(special_characters, k=n_special if n_special is not None else 1)
    extra = random.choices(lowercase_characters +
                           uppercase_characters +
                           number_characters +
                           special_characters,
                           k=required_length - n_lowercase - n_uppercase - n_numbers - n_special)

    all = lower + upper + numbers + special + extra

    random.shuffle(all)

    password = ''.join(all)

    return password

# --------------------------------------------------------------------

if __name__ == '__main__':

    print(generate_password())

    print(generate_password(6, 0, 6, 0, 0))

    print(generate_password(6, n_numbers=6))