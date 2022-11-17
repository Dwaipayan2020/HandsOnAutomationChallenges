num_map = {0: 'zero', 1: 'one', 2: 'two', 3: 'three',
           4: 'four', 5: 'five', 6: 'six', 7: 'seven',
           8: 'eight', 9: 'nine'}

digi = int(input())


def get_digi_key(digit, dict_):
    if 0 < digit < 9:
        return dict_[digit]


print(get_digi_key(digi, num_map))
print('\nAll keys of num_map dictionary:\n', num_map.keys(), end='\n')
print('\nAll values of num_map dictionary:\n', num_map.values(), end='\n')
print('\nAll value pairs of num_map dictionary:\n', num_map.items())
