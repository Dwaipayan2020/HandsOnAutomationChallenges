"""WAF get_si() that takes Principle, Rate and Time
as arguments and returns the Simple
Interest.
"""


def get_si(p, r, t) -> float:
    return (p * r * t) / 100


principal = float(input('Enter Principal amount:\n'))
time = float(input('Enter Interest Period in Years:\n'))
rate = float(input('Enter Rate Of Interest:\n'))

print('Simple interest is : ', get_si(principal, rate, time))
