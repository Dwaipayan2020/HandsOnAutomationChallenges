from collections import Counter

available_items = None
available_shoes = None
customer_orders = list()
order_items_list = list()
N = 0

X = int(input())
if 0 < X <= 1000:
    available_shoes = list(map(int, input().split(' ', X - 1)))
    available_items = Counter(available_shoes).items()
    N = int(input())
if 0 < N <= 1000:
    for _ in range(N):
        ip_sz_prc = input()
        # ip_prc = input()
        sz_prc_lst = ip_sz_prc.split(' ', 1)
        customer_orders.append(tuple(map(int, sz_prc_lst)))

    for cus_ord in customer_orders:
        order_items_list.append(cus_ord[0])

    ordered_items = Counter(order_items_list).items()

    purchased_items_data = {k1: min(v1, v2) for k1, v1 in available_items for k2, v2 in ordered_items if k1 == k2}
    min_count = 0
    items_invoice = list()
    for k, v in purchased_items_data.items():
        for shoe in customer_orders:
            if k == shoe[0]:
                items_invoice.append(shoe[1])
                min_count += 1
            if min_count == v:
                break
        if min_count != 0:
            min_count = 0
    gross_total_price = sum(items_invoice)
    print(gross_total_price)
