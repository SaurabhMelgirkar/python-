
#multi -threading
#1] process based multi tasking
# 2] thread based multi tasking
"""
import threading
print(threading.current_thread())
print(threading.current_thread().name)
print(threading.current_thread().ident)
#threading.current_thread().setName("python")
#print(threading.current_thread().getName())
"""
"""
import threading
from threading import *
class Mainclass(Thread):
    def run(self):
        for i in range(4):
            print(" python class")
            print(threading.current_thread())
o=Mainclass()
o.run()

for i in range(4):
    print("webtech class")
    print(threading.currentThread())

"""
"""
import threading
from threading import *
def fun(n):
    for i in range(n):
        print("python class")
        print(threading.current_thread())
t=Thread(target=fun,args=(3,))
t.start()
"""
"""
import threading
from threading import *
def fun():
    for i in range(4):
        print("python class")
        print(threading.current_thread())
t=Thread(target=fun,)
t.start()
"""
"""
import threading
from threading import *
def fun(*m,**n):
    for i in range(2):
        print(n)
        print(m)
        print(threading.current_thread())
        print(threading.current_thread().name)
t=Thread(target=fun,args=(3,),kwargs={"n":1})
"""
"""
def fun3():
    for i in range(10):
        print(i)
        
t.start()
#fun(3,n=2))
#(fun3())
#print(x)
"""
#active thread count
"""
import threading
from threading import *
import time
def demo():
    print(current_thread().getName(),"started")
    time.sleep(3)
    print(current_thread().getName(),"ended")
print("active thread count",active_count())
t1=Thread(target=demo,name="childThread1")
t2=Thread(target=demo,name="childThread2")
t1.start()
t2.start()
time.sleep(3)
print("active thread number",active_count())

"""
"""
import threading
from threading import *
import time
def demo():
    print(current_thread().name,"start")
    time.sleep(3)
    print(current_thread().name,"ended")
print("test count is",active_count())
a=Thread(target=demo,name="first")
a.start()
#a1=Thread(target=demo,name="first")
#a1.start()
print("thread count is",active_count())
time.sleep(3)
print("current number is ",active_count())
"""
#is alive
"""
import threading
from threading import *
import time
def demo():
    print(current_thread().name,"start")
    time.sleep(3)
    print(current_thread().name,"ended")
print("test count is",active_count())
a=Thread(target=demo,name="first")
a1=Thread(target=demo,name="second")
a.start()
a1.start()
print(a.name,"thread is",a.is_alive())
print(a1.name,"thread is",a1.is_alive())
time.sleep(3)
print("thread is ",a.is_alive())
"""

#join method
"""
import threading
from threading import *
import time
def spam():
    for i in range(2):
        print("hello python")
a=Thread(target=spam)
a.start()
a.join()
for i in range(2):
    print("hello java")
"""
# demon threads - the threads which are running in the background are called as demon threads
#the main objective of demon thread is to provide support for non demon threads (mainthread)
#ex-garbage collector 
# whenever main thread runs with low low memory immeditly pvm runs garbage collector to destroy object and to provide free memory so that 
#so that main thread can continue to its execution without having any memory problem
# we can check weather thread is demon or not by using isdemon() method of thred class or by using demon property
"""
import threading
from threading import *
print(current_thread().isDaemon())
"""
#demon is depending on main thread
#it is for supporting purpose

from threading import *
l=Lock()
def Test(name):
    l.acquire()
    for i in range(3):
        print("good afternoon")
        print(name)
    l.release()
t=Thread(target=Test,args=("saurabh",))
s=Thread(target=Test,args=("raju",))
t.start()
s.start()
