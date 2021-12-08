def print_goodmorning(name):
    print('Goodmorning %s' % name)
    print('How are you today?')
    print('Have a great day!')

def book_flight(fromairport, toairport, numadults=1, numchildren=0):
    print("\nFlight booked from %s to %s" % (fromairport, toairport))
    print("Number of adults: %d" % numadults)
    print("Number of children: %d" % numchildren)

def calculate_bmi(weight, height):
    bmi = weight / height ** 2
    return bmi

def get_all_indeces(values, value_to_look_for):
    all_indeces = []
    for i, value in enumerate(values):
        if value == value_to_look_for:
            all_indeces.append(i)
    return all_indeces

def my_divmod(n1, n2):
    div = n1 // n2
    mod = n1 % n2
    return div, mod

# ------------------------------------------------------------

if __name__ == '__main__':

    name = 'Peter'

    print_goodmorning('Rogier')

    # book_flight('AMS', 'LHR')
    # book_flight(numchildren=10, toairport='LHR', fromairport='AMS')

    # print( calculate_bmi(90, 1.80) )
    my_bmi = calculate_bmi(90, 1.80)

    # print( get_all_indeces([1,2,3,4,5,5,5,], 5) )

    # print( my_divmod(17, 6) )

    print(name)