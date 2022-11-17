find_older = lambda x, y, z: x if x > y and x > z else y if y > x and y > z \
    else z if z > y and z > x else False
find_younger = lambda x, y, z: x if x < y and x < z else y if y < x and y < z \
    else z if z < x and z < y else False

find_equal_older = lambda x, y, z: x if x > z and y > z and x == y != z \
    else y if y > x and z > x and y == z != x else z if z > y and x > y and z == x != y else False

find_equal_younger = lambda x, y, z: x if x < z and y < z and x == y != z \
    else y if y < x and z < x and y == z != x else z if z < y and x < y and z == x != y else False

check_if_equal_older = True
check_if_equal_younger = True
age_ = 0


def find_oldest_person(*age):
    get_age_list = age
    older = list()
    for current_list in get_age_list:
        result = find_older(get_age_list[0][0], get_age_list[0][1], get_age_list[0][2])
        if not result:
            print('All persons are of equal age for the current input.')
            check_if_equal_older = find_equal_older(get_age_list[0][0], get_age_list[0][1], get_age_list[0][2])
            check_if_equal_younger = find_equal_younger(get_age_list[0][0], get_age_list[0][1], get_age_list[0][2])

        if not check_if_equal_older:
            return
        elif not check_if_equal_younger:
            return check_if_equal_older

        print('Older person has age in this input: ', result, end='\n')
        older.append(result)
    return older[0]


def find_youngest_person(*age):
    get_age_list = age
    younger = list()
    for current_list in get_age_list:
        result = find_younger(get_age_list[0][0], get_age_list[0][1], get_age_list[0][2])
        if not result:
            print('All persons are of equal age for the current input.')
            check_if_equal_older = find_equal_older(get_age_list[0][0], get_age_list[0][1], get_age_list[0][2])
            check_if_equal_younger = find_equal_younger(get_age_list[0][0], get_age_list[0][1], get_age_list[0][2])

        if not check_if_equal_younger:
            return
        elif not check_if_equal_older:
            return check_if_equal_younger

        print('\nYoungest person has age: ', result, end='\n')
        younger.append(result)
    return younger[0]


input_age_list = tuple(map(int, input().split()))

find_oldest_person(input_age_list)
find_youngest_person(input_age_list)
