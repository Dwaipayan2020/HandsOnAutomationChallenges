""" WAP to input a string and
store ASCII values of all characters
in a tuple.
"""

str = str(input('Input a String:\n'))
lst = list()
ascii_to_str = list()
for ch in str:
    ascii_ch = ord(ch)
    print(ch, ascii_ch, end='\n')
    lst.append(ascii_ch)
    # ascii character to character
    # ascii_to_str.append(chr(ascii_ch))
tpl = tuple(lst)
print(tpl)
# print(ascii_to_str)
