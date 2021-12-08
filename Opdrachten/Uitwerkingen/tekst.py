def calculate_bmi(weight, height):
    bmi = weight / height ** 2
    return bmi


# ---------------------------------

height = float(input('Enter height: '))
weight = float(input('Enter weight: '))

calculated = calculate_bmi(weight, height)

print(f'Your BMI is {calculated:.1f}')
