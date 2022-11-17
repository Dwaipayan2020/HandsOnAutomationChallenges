""" WAP get_ci() that takes Principle, Rate and Time as arguments
and returns the
Compound Interest.
"""
import math


def get_ci(p, r, n, t) -> float:
    interest = (r / n) * 0.01
    period = n * t

    amount = p * math.pow(1 + interest, period)
    ci = amount - p
    return ci


principal = float(input('Enter Principal amount:\n'))
rate = float(input('Enter Rate Of Interest:\n'))
num = int(input('Enter Compound Quantity Per Year:\n'))
time = float(input('Enter Interest Period in Years:\n'))
comp_interest = get_ci(principal, rate, num, time)

print('Compound interest is : ', "{:.3f}".format(comp_interest))
print('Final amount becomes : ', "{:.3f}".format(comp_interest + principal))
