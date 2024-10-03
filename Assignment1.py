"""
s="welcome to my vlog"
print(s)
x=s[3:7:1]
x1=s[-12:-16:-1]
x2=s[-12:2:-1]
x3=s[3:-11:1]
x4=s[8:11:1]
x5=s[-9:-11:-1]
x6=s[8:-8:1]
x7=s[0:3:1]
x8=s[-16: :-1]
x9=s[0:-15:1]
x10=s[13: :1]
x11=s[-1:-5:-1]
x12=s[-4:13:1]
x13=s[3:7:3]
x14=s[-12:-16:-3]
x15=s[0:4:3]
x16=s[-15:-19:-3]
print(x16)
"""
#armstrong number
"""
a=370
while a>0:
    n1=a%10
    n=a//10
    n2=n%10
    n3=n//10
    res=n1**3+n2**3+n3**3
if res==a :
    print(f"{a} is a armstrong number"  )
else:
    print(f"{a} is not armstronmg number")
        

#print(n4)
"""
#armstrong
"""
a=int(input("enter the number"))
temp=a
sum=0

while temp>0:
    x=temp%10
    sum+=x**3
    temp//=10
    #print(sum)
if a==sum:
    print(f"{a} is armstrong")
else:
    print(f"{a} is not armstrong")
"""

#parameterized decorator

"""
def pretify(symbol):
    def decorator(func):
        def wrapper(*args,**kwrgs):
            print(symbol*len(*args,**kwrgs))
            func(*args,**kwrgs)
            print(symbol*len(*args,**kwrgs))
        return wrapper
    return decorator
@pretify("==")
def name(name):
    print(name)
@pretify("--")
def city(city):
    print(city)
name("saurabh")
city("pune")
"""
"""
import time
def outermost(m,n):
    def outer(func):
        def inner(*args):
            print(m)
            time.sleep(n)
            func(*args)
        return inner
    return outer

@outermost("addition operation",1)
def add(a,b):
    print(a+b)
@outermost("substraction operation",2)
def sub(a,b):
    print(a-b)
@outermost("multiplication operation",3)
def mul(a,b):
    print(a*b)
add(2,1)
sub(2,1)
mul(2,1)
"""
#module in python

"""
import datetime
x=datetime.datetime.now()


print(x)
y1=x.strftime("%y")
y2=x.strftime("%I")
print(y2)
print(y1)
"""
#random module
"""
import random
print(random.random())
print(random.randint(2,5))
print(random.randrange(2,5))#included start number exclude ending number
print(random.uniform(3,7))#it will included both numbers but output will be in decimal format
print(random.choice([1,2,3,4,5]))
"""
"""
from random import *
def otp():
    otp=" "
    for i in range (6):
        otp+=str(randint(0,9))
    print(otp)
otp()
"""
"""
from random import *
#import regex
def OTP():
    otp=" "
    for i in range(2):
        otp+=str(randint(0,9))
    for i in range(2):
        otp+=chr(randint(65,90))
    for k in range(2):
        otp+=chr(randint(97,122))
    print(otp)
OTP()
"""
"""
import math as x
print(x.fabs(-2))
print(x.factorial(5))
print(x.floor(2.3455))
print(x.fsum([1,2,3,4]))
print(x.ceil(1.22))
print(x.pow(2,3))
print(x.cbrt(27))
print(x.sqrt(16))
print(x.modf(10))
print(x.pi)
"""
"""
import calendar
#print(calendar.calendar(2024))
#print(calendar.month(2024,8))
#print(list(calendar.month_name))
#print(calendar.weekheader(3))
calendar.setfirstweekday(2)
print(calendar.weekheader(3))
"""






