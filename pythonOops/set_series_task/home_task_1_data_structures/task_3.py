"""Read help for zip and write a program that has two lists
l1 = [1,2,3,4]
l2 = [10,20,30,40]
And converts them to a dictionary d containing { 1:10,2:20 …….}
"""

l1 = [1, 2, 3, 4]
l2 = [10, 20, 30, 40]


def zip_into_dict(lst1, lst2):
    try:
        if lst1 is not None and lst2 is not None:
            return dict(zip(lst1, lst2))
        else:
            return
    except ValueError as v_err:
        print(v_err)


print(zip_into_dict(l1, l2))
