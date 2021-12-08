from decimal import Decimal

def frange(start, stop, step=1.0, endpoint=False):
    numbers = []
    number = start
    while True:
        numbers.append(number)
        number = round(number + step, 10)
        if endpoint:
            if number > stop:
                break
        else:
            if number >= stop:
                break
    return numbers

def float_range(arg1 = 0, arg2 = None, step=1, endpoint=False):
    if arg2 is None:
        start = 0
        stop = arg1
    else:
        start = arg1
        stop = arg2

    number = start + step * 0   # to set type to the same type as step
    while True:
        yield number
        number += step
        if endpoint:
            if number > stop:
                break
        else:
            if number >= stop:
                break

def decimal_range(arg1 = 0, arg2 = None, arg3=1, endpoint=False):
    if arg2 is None:
        start = Decimal(0)
        stop = Decimal(str(arg1))
    else:
        start = Decimal(arg1)
        stop = Decimal(str(arg2))

    step = Decimal(str(arg3))

    number = start + step * 0   # to set type to the same type as step
    while True:
        yield float(number)
        number += step
        if endpoint:
            if number > stop:
                break
        else:
            if number >= stop:
                break

# ------------------------------------------------------

if __name__ == '__main__':

    print('frange(1, 10) => ', list(frange(1, 10)))
    print('frange(1, 10, endpoint = True) => ', list(frange(1, 10, endpoint = True)))
    print('frange(1, 10, 2) => ', list(frange(1, 10, 2)))
    print('frange(1, 10, 0.5) => ', list(frange(1, 10, 0.5)))
    print('frange(1, 10, 0.5, endpoint = True) => ', list(frange(1, 10, 0.5, endpoint = True)))
    print('frange(1, 10, 0.2, endpoint = True) => ', list(frange(1, 10, 0.2, endpoint = True)))

    # print('float_range(10) => ', list(float_range(10)))
    # print('float_range(1, 10) => ', list(float_range(1, 10)))
    # print('float_range(1, 10, endpoint = True) => ', list(float_range(1, 10, endpoint = True)))
    # print('float_range(1, 10, 2) => ', list(float_range(1, 10, 2)))
    # print('float_range(1, 10, 0.5) => ', list(float_range(1, 10, 0.5)))
    # print('float_range(1, 10, 0.5, endpoint = True) => ', list(float_range(1, 10, 0.5, endpoint = True)))
    # print('float_range(1, 10, 0.2, endpoint = True) => ', list(float_range(1, 10, 0.2, endpoint = True)))
    #
    # print('decimal_range(1, 10, 0.2, endpoint = True) => ', list(decimal_range(1, 10, 0.2, endpoint = True)))
