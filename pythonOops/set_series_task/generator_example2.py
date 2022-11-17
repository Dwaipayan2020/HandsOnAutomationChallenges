def my_range(start, end):
    """This is generator"""
    current = start
    while current < end:
        try:
            yield current
            current += 1
        except StopIteration:
            break


nums = my_range(1, 10)
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(nums.__next__())


