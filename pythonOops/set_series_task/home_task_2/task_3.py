"""Write a function map_multiple that takes a list of functions/lambdas
 as first argument and a sequence type as second argument.
The function picks first lambda from list, applies it to first element,
then applies the second function to the result of first one and
Similarly it does for each element and generates
a mapping of input to output .

            def map_multiple(functs, sequence):
             # write definition here

Ex: let list of lambdas be from question 1 and the list on numbers
 be [1,2,4]
 So first function gives [1, 4, 16]
 Second gives [1, 0.25, 0.0625]
 Third gives [-1, -0.25, -0.0625]. Which is the final result

"""

import sys

# from functools import reduce

num_list = [1, 2, 4, 8]
func_sqr_lam = lambda x: x ** 2
func_inverse_lam = lambda x: 1 / x
func_negate_lam = lambda x: (-x)
# func_max_val = lambda n, m: n if n > m else m

func_list = [func_sqr_lam, func_inverse_lam, func_negate_lam]


def display_new_sequence(func, sequence):
    """write definition here """
    if func == func_sqr_lam:
        sys.stdout.write('------------Printing Squares of input--------------\n')

    elif func == func_inverse_lam:
        sys.stdout.write('------------Printing inverse of input--------------\n')

    elif func == func_negate_lam:
        sys.stdout.write('------------Printing Negates of input--------------\n')

    # elif func == func_max_val:
    #     sys.stdout.write('------------Printing maximum value  of given input--------------\n')
    #     max_val = reduce(func_max_val, num_list)
    #     print(max_val)

    else:
        raise ValueError

    [print(func(x)) for x in sequence]
    # if func != func_max_val:
    #     [print(func(x)) for x in sequence]


def map_multiple(functs, sequence):
    """write definition here """
    s = sequence
    for func in functs:
        display_new_sequence(func, s)
        s = list(map(func, s))


map_multiple(func_list, num_list)
