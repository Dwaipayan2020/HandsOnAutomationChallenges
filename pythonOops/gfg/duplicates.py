def find_duplicates(arr, n):
    # code here
    a1 = arr[:n]
    l1 = len(a1)
    duplicate_items = set()
    count = 0
    i = 0

    while i < l1:
        if a1.count(a1[i]) > 1:
            count = 1
        if count > 0:
            duplicate_items.add(a1[i])
            count = 0
        i += 1
    if duplicate_items is None:
        return [-1]
    else:
        return ' '.join(list(map(str, duplicate_items)))


print(find_duplicates([2, 3, 1, 2, 3], 4))
