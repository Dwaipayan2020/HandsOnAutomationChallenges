if __name__ == '__main__':
    n = int(input())
    lst2 = list()
    if n >= 2 or n <= 10:
        arr = map(int, input().split(' ', n))
        lst2 = [item for item in list(arr) if item >= -100 if item <= 100]
        lst2.sort()

    m = [item for item in lst2 if item != max(lst2) if item >= -100 if item <= 100][-1]
    print(m)
