"""WAP to input a string and split it into 2 halves.
The string can be of any length
Ex-1: Input = “String”
S1 = Str
S2 = ing
Ex-2: Input = “words”
S1 = wo
S2 = ds

"""
input_str = input()
s_1 = None
s_2 = None
l1 = len(input_str)
break_i = 0
if l1 % 2 == 0:
    break_i = int(l1 / 2)
    s_1 = input_str[:break_i]
    s_2 = input_str[break_i:]
elif l1 % 2 != 0:
    break_i = int(l1 // 2)
    s_1 = input_str[:break_i]
    s_2 = input_str[break_i+1:]
print(s_1, s_2)
