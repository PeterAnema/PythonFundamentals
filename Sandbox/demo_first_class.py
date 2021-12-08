
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def diff(n1, n2):
    return abs(n1 - n2)

def do_it(arg1, arg2, f):
    return f(arg1, arg2)

# ---------------------------------------------

print( do_it(6, 7, add) )
print( do_it(6, 7, subtract) )
print( do_it(6, 7, diff) )
