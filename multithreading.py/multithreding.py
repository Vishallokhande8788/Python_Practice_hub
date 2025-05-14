# by using function  craete thread 
'''
from threading import *

def sayHello():
    for i in range(10):
        print('child Thread')

t = Thread(target=sayHello)
t.start()
for i in range(10):
    print('main thread')
    '''

'''
# create class by extebding thread class

import time
from threading import *

class MyThread(Thread):
    def run(self):
        name = 'Vishal LOkhande'
        for n in name:
            print(n)
            time.sleep(1)

t=MyThread()
t.start()
for i in range(6):
    print(i)
    time.sleep(1)
    '''
'''
# without extending thread class


import time
from threading import *

class MyThread:
    def print_char(self):
        name = 'Vishal LOkhande'
        for n in name:
            print(n)
            time.sleep(1)

t=MyThread()
thread = Thread(target=t.print_char)
Thread.start()
for i in range(6):
    print(i)
    time.sleep(1)
    '''

