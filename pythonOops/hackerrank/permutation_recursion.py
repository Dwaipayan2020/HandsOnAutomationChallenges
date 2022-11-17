"""Permutation using recursion
"""


def permute_str(ip_str, start, end):
    x = list(ip_str)
    if start == end - 1:
        print(ip_str)
    else:
        for current in range(start, end):
            x[start], x[current] = x[current], x[start]
            permute_str(''.join(x), start + 1, end)


permute_str(['A', 'B', 'C'], 0, 3)
