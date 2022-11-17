"""WAP to input a number and check if number is divisible by
both 5 and 7.
"""


def is_divisible(dividend, divisor=1):
    if dividend % 5 == 0:
        print(f'{dividend} is exact divisible by 5.')
    else:
        print(f'{dividend} is not exact divisible by 5!')
    if dividend % 7 == 0:
        print(f'{dividend} is divisible by 7.')
    else:
        print(f'{dividend} is not exact divisible by 7!')

    return dividend % divisor == 0


print(is_divisible(35))
# inp = list(map(int, input('Test with inputs example:\n').split(' ', 1)))
print('Please find the below examples:\n')
inp = int(input())
print(is_divisible(inp))
