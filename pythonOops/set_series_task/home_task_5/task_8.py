"""WAP to input number of seconds and print
in days, hours, minutes and seconds
ex: input = 10000
Output = 0 day 2 hour 46 minute 40 second
"""

from datetime import datetime

t_stamp = 10000


# date_time = datetime.fromtimestamp(timestamp)
# d = date_time.strftime("%m/%d/%Y, %H %M %S")
# print(d)


def get_day_datetime_from_timestamp(timestamp):
    date_time = datetime.fromtimestamp(timestamp)
    print("Date time object:", date_time)
    day_of_month = date_time.strftime("%d")
    hour_of_day = date_time.strftime("%H")
    min_of_hour = date_time.strftime("%M")
    sec_of_min = date_time.strftime("%S")
    print(day_of_month, ' day ', hour_of_day, ' hour ', min_of_hour, ' minute ', sec_of_min, ' second ')


get_day_datetime_from_timestamp(t_stamp)
