""""""


class Student:
    marks = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_marks(self, marks_list):
        self.marks = marks_list

    def get_avg_marks(self):
        avg_marks = float(0)
        try:
            if self.marks:
                n = len(self.marks)
                avg_marks = sum(map(float, self.marks)) / n
            return avg_marks
        except ZeroDivisionError as zdv_err:
            print(zdv_err)

    def print_details(self):
        print(f'\nStudent named {self.name} of age {self.age} has got average marks, {self.get_avg_marks()}.\n')


if __name__ == '__main__':
    s = Student('abc', 20)
    s.set_marks([80, 60, 90, 70, 99])
    s.print_details()
