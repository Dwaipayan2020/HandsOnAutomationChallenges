"""This context manager will automatically acquire
   and release objects for you.
"""


class PoolManager:
    def __init__(self, pool):
        self.pool = pool

    def __enter__(self):
        self.obj = self.pool.acquire()
        return self.obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.pool.release(self.obj)


class Reusable:
    def test(self):
        print(f'Using object {id(self)}')


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

with PoolManager(pool) as r:
    r.test()

with PoolManager(pool) as r2:
    r.test()

with PoolManager(pool) as r3:
    r.test()

"""Using object 2314104254320   ---> same memory address allocated for 'r' object
   Using object 2314104254320   ---> same memory address allocated for 'r2' object
   Using object 2314104254320   ---> same memory address allocated for 'r3' object
"""