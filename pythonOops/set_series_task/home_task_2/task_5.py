""" Assume a list containing heights ft and inches
in the form of a list of string
Example : l = [‘5ft10in’, ‘5ft’, ….]
Write a function to convert the heights to meter.
Use map function along with your function to convert everything to m.
"""

inch_to_feet = lambda x: x / 12
feet_to_meter = lambda y: y * 0.3048
heights = ['5ft10in', '6ft', '5ft8in']


def convert_height_to_meter(height_in_word):
    inch = 0
    tmp_ft = height_in_word.split('ft')[0]
    tmp_in = height_in_word.split('ft')[1].split('in')[0]
    if not tmp_in == '':
        inch = int(tmp_in)

    if not tmp_ft == '':
        feet = int(tmp_ft) + inch_to_feet(inch)

    else:
        raise ValueError

    return "{:.3f}".format(feet_to_meter(feet))


heights_in_meter = list(map(lambda h: convert_height_to_meter(h), heights))
print(heights_in_meter)
