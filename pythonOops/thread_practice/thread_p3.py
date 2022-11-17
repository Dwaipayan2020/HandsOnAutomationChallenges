"""Creating a Thread by creating any custom child Class
to a thread class and using constructor.
"""

from threading import Thread


class ChildThreadClass(Thread):
    def __init__(self, a):
        Thread.__init__(self)
        print('Child Thread running', a)

    def run(self):
        print('\nRun method started using child thread.')


t = ChildThreadClass(10)
t.start()
# print(t.name)

for j in range(5):
    print('\nMain Thread')
