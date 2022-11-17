"""Named Tuple Example  --  Hacker rank
"""

from collections import namedtuple

#
# stu1 = Student(ID='0010', MARKS=60, NAME='Shankar', CLASS=10, )
# stu2 = Student('0011', 70, 'Ravi', 10)

# print(stu1.ID, stu1.NAME, stu1.MARKS, stu1.CLASS, end='\n')
# print(stu2.ID, stu2.NAME, stu2.MARKS, stu2.CLASS, end='\n')
#
# print(help(Student))

# change_lam  = lambda x: isinstance(x, int)
#
# fl_itm = filter(change_lam, stu1)
#
# print(list(fl_itm))
# print('-------------- My code here ------------------')
student_records = set()
avg_marks = 0
N = int(input())
if 0 < N <= 100:
    fields = str(input())
    Student = namedtuple('Student', fields)
    for _ in range(N):
        record = str(input()).split(' ', 3)
        stu = Student(*record)
        student_records.add(stu)
    try:
        avg_marks = float('{:.2f}'.format(sum(list(map(int, [stu.MARKS for stu in student_records]))) / N))
    except ValueError as val_error:
        print(val_error)
    print(avg_marks)
