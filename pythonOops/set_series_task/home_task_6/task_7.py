"""WAF: days_in_month() that take name of month
 in 3 character format(MMM), and year (YYYY)
as arguments and returns
the number of days in the month.
"""

import calendar
import datetime as dt
from datetime import datetime
import random

MONTHS = {'JAN': '01', 'FEB': '02', 'MAR': '03',
          'APR': '04', 'MAY': '05', 'JUNE': '06',
          'JUL': '07', 'AUG': '08', 'SEP': '09',
          'OCT': '10', 'NOV': '11', 'DEC': '12'
          }


def get_an_random_date_obj(year_yyyy, month_mmm):
    month_index = None
    for month in MONTHS.items():
        if month_mmm.upper().__contains__(month[0]):
            month_index = month[1]

    any_day = random.randint(1, 28)
    random_date = f'{any_day}/{month_index}/{year_yyyy}'
    time_hr_secs = str(datetime.now()).split(' ')[1][0:8]
    date_tm_str = f'{random_date} {time_hr_secs}'
    date_time_obj = datetime.strptime(date_tm_str, '%d/%m/%Y %H:%M:%S')
    return date_time_obj


# current_date_obj = dt.date.today()
month_name = str(input('Enter month name as --> (MMM):\n'))
year_value = int(input('\nEnter year value as --> (YYYY):\n'))
custom_date_obj = get_an_random_date_obj(year_value, month_name)
daysInMonth = calendar.monthrange(custom_date_obj.year, custom_date_obj.month)[1]
print(daysInMonth)
