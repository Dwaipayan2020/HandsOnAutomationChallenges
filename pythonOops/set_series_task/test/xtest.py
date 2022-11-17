# length = int(input('Please enter length:\n'))
# breadth = int(input('\nPlease enter breadth:\n'))

check_sqr = lambda x, y: x == y and not x <= 0 and not y <= 0
check_rect = lambda x, y: x != y and not x <= 0 and not y <= 0


def check_p_gram(l, b):
    is_sqr = check_sqr(l, b)
    is_rect = check_rect(l, b)

    if is_sqr:
        print('Its a square')
    elif is_rect:
        print('Its a rectangle.')
    if is_sqr or is_rect:
        return True
    else:
        print('Neither rectangle or neither square.')
        return None

#
# check_p_gram(length, breadth)
