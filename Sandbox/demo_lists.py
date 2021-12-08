

numbers = [1.0, 5.3, 3, 4, 7, 2]

for number in numbers:
    print(number)


print(numbers[0])


squared = []
for n in numbers:
    squared.append(n ** 2)


squared = [n ** 2 for n in numbers]



print(squared)