def calculate_bmi(weight_in_kg, height_in_meter):
    try:
        sq_height = float(height_in_meter * height_in_meter)
        person_bmi = float(weight_in_kg / sq_height)
        return person_bmi
    except ValueError as val_error:
        print(val_error)
    except ZeroDivisionError as zero_div_err:
        print(zero_div_err)


is_normal_weight = lambda x: 18.5 < x < 25
is_under_weight = lambda x: 0 < x < 18.5
is_over_weight = lambda x: 25 <= x <= 29.9
is_obese = lambda x: 29.9 < x < 100

try:
    weight = float(input('\nEnter weight in kg:\n'))
    height = float(input('Enter height in cm:\n')) / 100
    bmi = calculate_bmi(weight, height)
    print('\nPerson bmi: ', bmi, 'kg/m^2', end='\n')

    if is_normal_weight(bmi):
        print('The person has normal weight/height ratio.')
    elif is_under_weight(bmi):
        print('The person is under-weight.')
    elif is_over_weight(bmi):
        print('The person is over-weight.')
    elif is_obese(bmi):
        print('The person is obese.')
    else:
        print('Incorrect weight or height data supplied for a human.')

except ValueError as v_err:
    print(v_err)
