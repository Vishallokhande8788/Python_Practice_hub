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

'''
# eg: multithreading 
import datetime
import time
from threading import *

def double(list):
    for i in list:
        print('Double is ',i*2)

def square(list):
    for i in list:
        print('Square is ',i*i)
        time.sleep(1)


nums = [1,2,3,4,5]

begining_time = datetime.datetime.now()

t1 = Thread(target=double, args=(nums,))
t2 = Thread(target=square, args=(nums,))

t1.start()
t2.start()

t1.join()
t2.join()

print('Total Time: ' , datetime.datetime.now() - begining_time)
'''

'''

#      join function
#      join function will wait for child thread to finish

#  eg: multithreading with join
import time 
from threading import *

def f1():
    for i in range(5):
        print('HELLO CHILD ')
        time.sleep(2)

t1 = Thread(target=f1)
t1.start()
t1.join() # join (5) : if parameter will be pass in join function then it will wait for child thread for 5 sec to finish (this line executed main thread )
for i in range(5):
    print('HELLO MAIN')
    time.sleep(2)
'''

'''

# eg : multithreading change thread name
from threading import *
import threading 

def f1():
    print("Hello ")
    print('current thread name : ',threading.current_thread().name)
    threading.current_thread().name = 'bhagesh'
    print('current thread name : ',threading.current_thread().name)


t1 = Thread(target=f1)
t1.start()

print('current thread name : ',threading.current_thread().name)
threading.current_thread().name = 'sushil'
print('current thread name : ',threading.current_thread().name)
'''


import time
from threading import *
l=Lock()

def wish (name):
    l.acquire()
    for i in range(5):
        print('Hello ',name)
        time.sleep(2)
    l.release()

t1 = Thread(target=wish, args=('vishal',))
t2 = Thread(target=wish, args=('sushil',))
t3 = Thread(target=wish, args=('bhagesh',)

t1.start()
t2.start()
t3.start()


# Multithreading allows you to run multiple tasks (called threads) at the same time within a single process.
# It’s useful when you're doing I/O-bound tasks like:

# Reading/writing files

# API calls

# Waiting for user input


import threading
import time

# Function 1 - Print numbers
def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(1)

# Function 2 - Print letters
def print_letters():
    for ch in ['A', 'B', 'C', 'D', 'E']:
        print(f"Letter: {ch}")
        time.sleep(1)

# Create threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# Start threads
t1.start()
t2.start()

# Wait for both to finish
t1.join()
t2.join()

print(" Both threads finished.")

# e. g 2

import threading
import time

# Function 1
def say_hello():
    for i in range(3):
        print("Hello")
        time.sleep(1)

# Function 2
def say_hi():
    for i in range(3):
        print("Hi")
        time.sleep(1)

# Create threads
t1 = threading.Thread(target=say_hello)
t2 = threading.Thread(target=say_hi)

# Start threads
t1.start()
t2.start()

# Wait for threads to complete
t1.join()
t2.join()

print(" Done with both threads!")
