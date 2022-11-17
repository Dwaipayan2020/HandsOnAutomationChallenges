"""WAP to find the length of
hypotenuse of a right-angled triangle,
input the height and base from user.
"""
import math as m


def get_hypotenuse(height, base) -> float:
    sum_squares = m.pow(height, 2) + m.pow(base, 2)
    hypotenuse = m.sqrt(sum_squares)
    return hypotenuse


h = int(input('Enter Height, (example- 60) :\n'))
b = int(input('Enter Base, (example- 80):\n'))
if b > h:
    print(f'Hypotenuse of right-angled triangle of '
          f'height {h} and base {b} is: ',
          get_hypotenuse(h, b))
else:
    print('As entered height is greater than base, '
          'height is changed to base and vice-versa.\n')
    print(f'Hypotenuse of right-angled triangle of '
          f'height {b} and base {h} is: ',
          get_hypotenuse(h, b))
