""" Use filter function to filter a list of numbers and strings
such that the result contains only numbers.
(Hint : Use isinstance method)
"""

person = ['Dwaipayan', 'Monday', 'April', '26', 29, 26041993, 1993]
func_filter = lambda x: isinstance(x, int)
filter_record = filter(func_filter, person)
print(list(filter_record))
