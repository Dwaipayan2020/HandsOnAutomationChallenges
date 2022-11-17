odd = [2, 4, 6, 8]
odd[0] = 1
print(odd)
odd[1:4] = [3, 5, 7]
print(odd)

n_list = ["Happy", [2, 0, 1, 5]]
print(n_list[0][1])
print(n_list[1][3])


def check_palindrome_string(inp_str):
    s = inp_str
    l0 = len(s)
    s1 = ''.join([s[i] for i in range(l0) if s[i] == s[-1 - i]])
    l1 = len(s1)

    if s1 == s and l1 == l0:
        print(f'{s} is palindrome.')
        return True
    else:
        print(f'{s} is not palindrome.')
        return False


s_ = 'hello'
# s_ = str(input('\nEnter a String to check if Palindrome:\n'))
print(check_palindrome_string(s_))

l_ = list()

for i in range(0, 21):
    if i % 5 == 0:
        l_.append(i)

t_ = tuple(l_)
print('newly created tuple: ', t_)

str_ = 'ncskndksjnskcns'

print(list(str_))
