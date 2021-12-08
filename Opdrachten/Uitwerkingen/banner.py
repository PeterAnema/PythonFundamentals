
def banner(s, fixed_width=0, filling_character='*', *args, **kwargs):
    n_width = max(fixed_width, len(s) + 6)
    n_spaces_before = (n_width - len(s) - 2) // 2
    n_spaces_after = n_width - 2 - n_spaces_before - len(s)
    line1 = filling_character * n_width + '\n'
    line2 = filling_character + ' ' * n_spaces_before + s.upper() + ' ' * n_spaces_after + filling_character + '\n'
    line3 = filling_character * n_width + '\n'
    return line1 + line2 + line3


# ------------------------------------------------

if __name__ == '__main__':

    user_input = input('Give me text: ')

    print( banner(user_input) )
    print( banner(user_input, 30) )
    print( banner(user_input, fixed_width=40, filling_character='#') )