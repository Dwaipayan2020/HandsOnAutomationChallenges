"""Write a function that takes a list of numbers
from user as argument and returns the sum of only odd numbers
 (Use only for loop. No need to use if statement).
 """


# Not using for loop or any if statement
# def get_sum_of(lst):
#     odd_items = filter(lambda k: k % 2 != 0, lst)
#     print(list(odd_items))
#     return sum(odd_items)

# Using for loop but not any if statement
def get_sum_of(lst):
    sum_val = 0
    odd_items = filter(lambda k: k % 2 != 0, lst)
    for i in odd_items:
        sum_val = sum_val+i
    return sum_val


print(get_sum_of(list(range(10))))
