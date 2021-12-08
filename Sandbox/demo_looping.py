

# number = 1
# while number < 10:
#     print(number)
#     number = number + 1
#
#
# for number in [4,3,2,6,1]:
#     print(number)
#
# for number in ['a','b','c','z']:
#     print(number)

# for number in range(1, 11, 2):
#     print(number)

magicnumber = 11

for i in range(1, 21):
    if i == magicnumber:
        break
    print(i)

for i in range(1, 21):
    if i == magicnumber:
        continue
    print(i)
