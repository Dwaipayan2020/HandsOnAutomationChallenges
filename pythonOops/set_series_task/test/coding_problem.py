"""
 Test Case 1: Input 5, 4 Expect result: 5, 4 - Rectangle
"""


class BaseSolution:
    length = int(input('Please enter length:\n'))
    breadth = int(input('\nPlease enter breadth:\n'))

    check_square = lambda x, y: x == y

    def check_p_gram(cls, l, b):
        is_true = bool(False)
        if l != 0 or b != 0:
            is_true = cls.check_square(l, b)

        if is_true:
            print('Its a square')
        else:
            print('Its a rectangle.')
