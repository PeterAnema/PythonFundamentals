

def add(n1, n2):
    return n1 + n2

add = lambda n1, n2: n1 + n2


numbers = [69,54,67,23,78,23,67,89,21,31]
print(numbers)

print( sorted(numbers) )

print( sorted(numbers, key = lambda number: number % 10) )

print( list( map(lambda number: number % 10, numbers) ) )