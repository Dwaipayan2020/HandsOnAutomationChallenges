"""WAF: is_alphabet() that takes a string argument
and returns True or False.
True if all characters in the string are alphabets
otherwise False.
(write code using for loop and if.
Do not use built-in functions)
"""
import re

s1 = input()
pattern = '[a-zA-Z\^\d]'


def is_alphabet(input_str) -> bool:
    i1 = ord('A')
    j1 = ord('Z')
    i2 = ord('a')
    j2 = ord('z')
    for ch in input_str:
        if ord(ch) < i1 and not (i1 <= ord(ch) <= j1 and i2 <= ord(ch) <= j2):
            print('Not Matched')
            return False
        elif ord(ch) > j2 and not (i1 <= ord(ch) <= j1 and i2 <= ord(ch) <= j2):
            print('Not Matched')
            return False
        else:
            pass

    print('Matched')
    return True


def check_if_alphabet(input_str) -> bool:
    if re.search(pattern, input_str):
        print('Matched')
        return True
    else:
        print('Not matched.')
        return False


assert is_alphabet(s1), 'Not an alphabet'
# assert check_if_alphabet(s1), 'Not an alphabet'
