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


s_ = str(input())
print(check_palindrome_string(s_))
