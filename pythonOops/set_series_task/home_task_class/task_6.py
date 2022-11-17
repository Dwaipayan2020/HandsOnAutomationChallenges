"""6. Create a class SelfManaged such that it keeps track
of the number of objects currently alive.
Create a class method
get_current_count(), that gives the number of objects
currently alive in memory.
"""


class SelfManaged:
    obj_count = 0

    def __init__(self):
        """Inside Constructor"""
        SelfManaged.obj_count += 1

    def __del__(self):
        """Inside Destructor"""
        SelfManaged.obj_count -= 1

    @classmethod
    def get_current_account(cls):
        return cls.obj_count


s_man1 = SelfManaged()
s_man2 = SelfManaged()
s_man3 = SelfManaged()
print(SelfManaged.get_current_account())
SelfManaged.__del__(s_man3)
# del s_man3
print(SelfManaged.get_current_account())
