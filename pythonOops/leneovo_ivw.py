"""
Write a function that reverses a string. The input string is given as an array of characters s.



You must do this by modifying the input array in-place with O(1) extra memory.



Example:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""

s = ["h", "e", "l", "l", "o"]
# s.reverse()
# print(s)
len_s = len(s)
# for i in range(len_s):
#     s[i] = s[-1 - i]
# new_lst = [s[-1-i] for i in range(len_s)]
print('Actual str given:\n', s)


def str_reverse(inp_str, start, end):
    if start == end:
        return inp_str
    else:
        inp_str[start], inp_str[end] = inp_str[end], inp_str[start]
        temp = inp_str
        str_reverse(temp, start + 1, end - 1)
        return inp_str


print('\nReversed lst is:\n', str_reverse(s, 0, len_s-1))
