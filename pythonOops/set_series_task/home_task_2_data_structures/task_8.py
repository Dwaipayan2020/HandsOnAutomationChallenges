s10 = 'Hello world'
s11 = 'Hello India'


def find_common_word(s1, s2):
    s1_lst = s1.split()
    s2_lst = s2.split()
    l1 = len(s1_lst)
    l2 = len(s2_lst)
    print('\n')
    return ' '.join([s1_lst[i] for i in range(l1) for j in range(l2) if s1_lst[i] == s2_lst[j]])


print(find_common_word(s10, s11))

s01 = str(input())
s02 = str(input())
print(find_common_word(s01, s02))
