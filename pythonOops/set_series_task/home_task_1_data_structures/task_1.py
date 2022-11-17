""" WAP to create a dictionary of numbers
mapped to their negative value for numbers from 1-5.
The dictionary should contain something like this:
{1:-1,2:-2,3:-3….}
Do with both with and without range based for loop.
"""


def create_map_dict(lower_limit, upper_limit):
    """Using range function
    """
    if lower_limit <= 0 or upper_limit <= 0:
        return

    record = {i: (-i) for i in range(lower_limit, upper_limit + 1)}
    return record


def create_map_record(lower_limit, upper_limit):
    """Without using range function
    """
    if lower_limit <= 0 or upper_limit <= 0:
        return
    i = lower_limit
    record = dict()
    while i < upper_limit + 1:
        record[i] = (-i)
        i += 1
    return record


print(create_map_dict(1, 5))
print(create_map_record(1, 5))
