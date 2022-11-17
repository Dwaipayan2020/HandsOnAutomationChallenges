"""Object-pool is responsible for managing pool of objects.
   We can implement it by using two lists.
   One list of object is in use and
   other list of objects are free.

"""


class Reusable:
    def test(self):
        print(f'Using object {id(self)}')


# obj1 = Reusable()
# obj1.test()
# obj2 = Reusable()
# obj2.test()


class ReusablePool:
    def __init__(self, size):
        self.size = size
        self.free = []
        self.in_use = []
        for _ in range(size):
            self.free.append(Reusable())

    def acquire(self) -> Reusable:
        if not self.free:
            raise Exception('No more objects are available')
        r = self.free[0]
        self.in_use.append(r)
        self.free.remove(r)
        return r

    def release(self, r: Reusable):
        self.in_use.remove(r)
        self.free.append(r)


pool = ReusablePool(2)

r = pool.acquire()
r2 = pool.acquire()

r.test()
r2.test()
"""Using object 1982396399328 --- r
   Using object 1982396399232 --- r2
"""
pool.release(r2)
r3 = pool.acquire()
r3.test()
"""Using object 2893151043440
   Using object 2893151043296   --- r2 (before release)
   Using object 2893151043296   --- r3 (acquired after r2 released)
"""
