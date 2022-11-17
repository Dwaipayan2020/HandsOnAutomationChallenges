"""WAP get_q_r() taking 2 numbers as parameters and
returns the quotient and remainder
in the form of a tuple.
"""


def get_q_r(param1, param2):
    q = param1 / param2
    r = param1 % param2
    quotient_ft = "{:0.2f}".format(q)
    remainder_ft = "{:0.2f}".format(r)
    return tuple([quotient_ft, remainder_ft])


dividend = float(input('Enter Dividend:\n'))
divisor = float(input('Enter Divisor:\n'))
print('Quotient, Remainder = ', get_q_r(dividend, divisor))
