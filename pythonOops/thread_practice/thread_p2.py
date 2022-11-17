"""Creating a Thread by creating any custom child Class
to a thread class.
"""

from threading import Thread


class ChildThreadClass(Thread):
    def run(self):
        for i in range(3):
            print('\nChild Thread')


t = ChildThreadClass()
t.start()
"""
Waits for the thread to end the current execution before running next thread. 
Using join method.
"""
t.join()
# print(t.name)

for j in range(5):
    print('\nMain Thread')
