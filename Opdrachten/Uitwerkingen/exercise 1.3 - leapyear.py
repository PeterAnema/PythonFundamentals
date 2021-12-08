
year = int(input('Give a year: '))

is_leapyear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(year, is_leapyear)
