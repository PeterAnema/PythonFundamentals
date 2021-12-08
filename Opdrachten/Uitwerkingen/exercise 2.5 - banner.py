
def banner(text):
    n = len(text)
    print('***' + '*' * n + '***')
    print('*  ' + text    + '  *')
    print('***' + '*' * n + '***')


def create_banner(text, c='*'):
    n = len(text)
    s  = c * (n + 6) + '\n'
    s += c + '  ' + text + '  ' + c + '\n'
    s += c * (n + 6)
    return s

def print_banner(text):
    print(create_banner(text, '+'))


# ----------------------------------------------------------

if __name__ == '__main__':

    name = input('Wat is jouw naam? : ')

    banner(name)

    print_banner(name)
