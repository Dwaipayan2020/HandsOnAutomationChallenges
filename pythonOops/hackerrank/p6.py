from collections import Counter

available_items = None
available_shoes = None
customer_orders = list()
order_items_list = list()
N = 0

X = int(input('enter the number of shoes:\n'))
if 0 < X <= 1000:
    available_shoes = list(map(int, input('enter size of shoes:\n').split(' ', X - 1)))
    print(Counter(available_shoes))

    print('available_shoes of sizes: ', Counter(available_shoes).items())
    available_items = Counter(available_shoes).items()
    N = int(input('\nenter number of customers:\n'))
if 0 < N <= 1000:
    for _ in range(N):
        ip_sz_prc = input('\nenter \'size price\' :\n')
        # ip_prc = input()
        sz_prc_lst = ip_sz_prc.split(' ', 1)
        customer_orders.append(tuple(map(int, sz_prc_lst)))

    for cus_ord in customer_orders:
        order_items_list.append(cus_ord[0])

    print('order_items_list : ', Counter(order_items_list))
    ordered_items = Counter(order_items_list).items()

    purchased_items_data = {k1: min(v1, v2) for k1, v1 in available_items for k2, v2 in ordered_items if k1 == k2}

    print(purchased_items_data)
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
    print('price_list: ', items_invoice)
    gross_total_price = sum(items_invoice)
    print('\nAmount of money earned by Raghu:\n', gross_total_price)
