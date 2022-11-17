is_abs_small = lambda x, y, z: x \
    if 0 < x < y < z or 0 < x < z < y \
    else y if z > x > y > 0 or x > z > y > 0 \
    else z if y > x > z > 0 or x > y > z \
    else False

is_abs_big = lambda x, y, z: x \
    if x > y > z > 0 or x > z > y > 0 \
    else y if y > x > z > 0 or y > z > x > 0 \
    else z if z > x > y > 0 or z > y > x > 0 \
    else False

is_small = lambda x, y, z: x \
    if y == z > x > 0 or z > (x == y > 0) or y > (x == z > 0) \
    else y if x == z > y > 0 or z > (y == x > 0) or x > (y == z > 0) \
    else z if x == y > z > 0 or y > (z == x > 0) or x > (z == y > 0) else False

is_big = lambda x, y, z: x \
    if x > y == z > 0 or x == y > z > 0 or x == z > y > 0 \
    else y if y > x == z > 0 or y == z > x > 0 or y == x > z > 0 \
    else z if z > x == y > 0 or z == x > y > 0 or z == y > x > 0 else False


def find_youngest_age(age_):
    age_list = age_
    if not is_abs_small(*age_list):
        if not is_small(*age_list):
            return
        else:
            result = is_small(*age_list)
            print('\nYoungest age or age-group in the group: ', result, end='\n')
    else:
        result = is_abs_small(*age_list)
        print('\nYoungest age in the group: ', result, end='\n')


def find_oldest_age(age_):
    age_list = age_
    if not is_abs_big(*age_list):
        if not is_big(*age_list):
            return
        else:
            result = is_big(*age_list)
            print('\nOldest age or age-group in the group: ', result, end='\n')
    else:
        result = is_abs_big(*age_list)
        print('\nOldest age in the group: ', result, end='\n')


age = None
try:
    age = list(map(int, input().split(' ', 2)))
    record_num = len(age)
    i = 0
    if record_num < 3:
        while i < 3 - record_num:
            i += 1
            age.append(0)
    for i in range(len(age)):
        if age[i] == 0 or age[i] < 0:
            age[i] = int(input('Please enter an age value which is not zero or not less than zero:\n'))
except ValueError as v_err:
    print(v_err, 'Age should be taken as an integer value. Please enter age for three people only!')

age_data = age
find_youngest_age(age_data)

find_oldest_age(age_data)
