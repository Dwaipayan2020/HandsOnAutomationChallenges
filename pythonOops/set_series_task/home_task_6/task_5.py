""" WAF: is_leap_year() that takes a year as input and returns
 True if year is leap year, otherwise
false.
"""


def is_leap_year() -> bool:
    year = int(input('Check if the year is leap year. Enter year:\n'))
    try:
        if year % 4 == 0:
            print(f'Yes, {year} is a leap year. is_leap_year ? -> ', True)
            return True
        else:
            print(f'No, {year} is not a leap year. is_leap_year ? -> ', False)
            return False
    except ValueError as value_error:
        print('Please enter year as integer.')
        print(value_error)


is_leap_year()
