

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def do_it(n1, n2, f):
    return f(n1, n2)



print(do_it(10, 7, add))
print(do_it(10, 7, subtract))
print(do_it(10, 7, multiply))

print(do_it(10, 7, lambda n1, n2: n1*10 + n2))
