data_copy = {'a': 54, 'b': 45, 'B': 60}
data = {'a': 54, 'b': 45, 'B': 60}

var = {k.lower(): data.get(k.lower(), 0) + data.get(k.upper(), 0) for k in data.keys()}
print('Example of Dictionary Comprehension ', var)

# updates the current dictionary
for k in data.keys():
    data[k.lower()] = 100
print('\nupdates the current dictionary --> data{}\n', data)

# creates new dictionary , doesn't update in current dictionary
var2 = {k.lower(): 100 for k in data_copy.keys()}
print('\ncreates new dictionary --> var2{} from data_copy {}\n', var2)
print('\n data_copy dictionary not impacted : \n', data_copy)


def update_dict(any_dict, v):
    for key in any_dict.keys():
        any_dict[key.lower()] = v
    print('\nInside update_dict function:\n', any_dict)


update_dict(data, 100)
