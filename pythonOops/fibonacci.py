def fibo(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        # temp_b = b
        # temp_a = a
        # a = temp_b
        # b = temp_a + temp_b
        # a, b = b, a + b
    return result


print(fibo(50))
