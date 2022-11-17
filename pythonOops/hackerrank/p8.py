""" Order Dict problem - Hacker Rank
"""
from collections import OrderedDict

check_prc_at_index = lambda x: x > 1
N = int(input())
basket = list()
basket_dict = OrderedDict()
for _ in range(N):
    ts = input().split()
    price = int(ts[-1])
    i = ts.index(ts[-1])
    if not check_prc_at_index(i):
        item = ts[0]
    else:
        item = ts[0] + ' ' + ts[1]
    tup = tuple([item, price])
    basket.append(tup)
    item_count = basket.count(tup)
    basket_dict[tup] = item_count

ordered_dict = {k[0]: k[1] * v for k, v in sorted(basket_dict.items(), key=lambda el: el[1])}

ordered_lst = [f'{k} {v}' for k, v in ordered_dict.items()]

for _ in ordered_lst:
    print(_)
