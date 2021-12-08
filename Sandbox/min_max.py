

# def min_max(values):
#     return min(values), max(values)

def min_max(values):
    minimum = values[0]
    maximum = values[0]
    for value in values[1:]:
        if value < minimum:
            minimum = value
        if value > maximum:
            maximum = value
    return minimum, maximum

#--------------------------------------------------

values = [6,2,8,3,5,7,1,4]

print(min_max(values))