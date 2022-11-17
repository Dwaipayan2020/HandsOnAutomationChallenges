full_name = input()
name_parts = full_name.split(' ', 1)
f_name = name_parts[0]
l_name = name_parts[1]
print(name_parts, 'first name: ', f_name, 'last name: ', l_name)
name_parts.reverse()
print(name_parts)
rev_l_nm_lst = list(name_parts[0])
rev_l_nm_lst.reverse()
rev_l_nm = ''.join(rev_l_nm_lst)
rev_f_nm_lst = list(name_parts[1])
rev_f_nm_lst.reverse()
rev_f_nm = ''.join(rev_f_nm_lst)
print(rev_l_nm, rev_f_nm)
