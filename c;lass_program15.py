
#multi threading rlog
"""
from threading import *
l=Lock()
r=RLock()
print("lock system1")
r.acquire()
print("lock system2")
r.acquire()
print("lock system 3")
r.release()
r.release()
"""
"""
from threading import *
import time
l=Lock()
def spam(name):
    l.acquire()
    for i in range(3):
        print(i)
        time.sleep(2)
        print(name)
    l.release()
t=Thread(target=spam,args=("python ",))
t1=Thread(target=spam , args=("web-tech",))
t.start()
t1.start()
"""
#semoforce
"""

from threading import *
import time
l=Semaphore(2)
def spam(name):
    l.acquire()
    for i in range(3):
        print(i)
        time.sleep(2)
        print(name)
    l.release()
t=Thread(target=spam,args=("python ",))
t1=Thread(target=spam , args=("web-tech",))
t2=Thread(target=spam , args=("java" ,))
t.start()
t1.start()
t2.start()
"""