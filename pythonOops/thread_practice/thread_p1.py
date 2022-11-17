"""Creating a Thread without using any Custom Class"""

from threading import Thread


def display():
    for i in range(5):
        print('\nChild Thread running')


t = Thread(target=display)
t.start()

for i in range(3):
    print('\nMain Thread running')
