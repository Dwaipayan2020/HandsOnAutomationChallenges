# nums = [7, 8, 9, 5]
# it = iter(nums)
# print(it.__next__())
# print(it.__next__())
# print(next(it))

class IteratorExample:
    """Now this IteratorExample is the iterator"""
    def __init__(self):
        """Initializing the counter"""
        self.num = 1

    def __iter__(self):
        """iter() will give you the object of iterator """
        return self

    def __repr__(self):
        return 'iterator object is returned.'

    def __next__(self):
        """next() will give the next value or next object."""
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration


iterator_example = IteratorExample()

"""Testing the condition where
the next method is being called in the function
in two different ways,
one--> in single line via direct call using iterator
two--> in for loop printing the iterable objects of the iterator
in each iteration.
So the power of using iterator is it remembers the previous
state and moves on to new object each time __next__() is
being invoked.
"""
print('Printing the first object or first value\n')
print(iterator_example.__next__())
print('\nPrinting the next objects in iteration via for loop')
for i in iterator_example:
    print(i)

