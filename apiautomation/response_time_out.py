import requests
from requests import ReadTimeout


def handle_timed_out_resp(delay, tout=None):
    try:
        print('\ndelay, timeout = ', delay, tout)
        response = requests.get(f'https://httpbin.org/delay/{delay}', timeout=tout)
        print('\nresponse2 status code: ', response.status_code)
        print('\nresponse2 : ', response)
    except ReadTimeout as read_time_out:
        print('\nException: ', read_time_out)


# getting a delayed response of delay time 6 secs, without applying time out
handle_timed_out_resp(delay=6)

# Invoking a delayed response of delay time 6 secs, when timeout ends in 3 secs

handle_timed_out_resp(delay=6, tout=3)

# Invoking a delayed response of delay time 3 secs, when there is time out of 5 seconds
handle_timed_out_resp(3, 5)
