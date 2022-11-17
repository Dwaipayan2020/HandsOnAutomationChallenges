# temp = 5
#
#
# def abc():
#     nonlocal temp
#     temp = temp + 5
#     print(temp)


temp_dict = {"a": 1, "e": 5, "c": 3, "b": 2, "d": 4}
sorted_dict = dict()


def update_dict(dict_name, val):
    dict_name[val[0]] = val[1]


for value in sorted(temp_dict.items(), key=lambda k: k[1]):
    # sorted_dict[value[0]] = value[1]
    update_dict(sorted_dict, value)

print(sorted_dict)

lst = sorted(temp_dict.items(), key=lambda k: k[1])
print(lst)
