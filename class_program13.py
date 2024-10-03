#decorator -meta programing
#we are doing modification without touching the main function
"""
def outer(funk):
    def inner(*args,**kwargs):
        print(f"we are performing addition")
        funk(*args,**kwargs)
    return inner
@outer
def add(a,b):
    print(a+b)
add(1,2)
"""
#wap before executiong i want to wait for 5 sec
"""
import time
def outer(funk):
    def inner(*args,**kwargs):
        time.sleep(5)
        print("inside")
        funk()
    
    return inner
@outer

def fun():
    time.sleep(3)
    print("hello")
fun()
"""
#wap before executing main print doing addition operarator later addition operator completed
"""
import time
def outer(funk):
    def inner(*args,**kwargs):
       # time.sleep(5)
        print("addition operation")
        funk(*args,**kwargs)
        print("addiition operator compleated")
    return inner
@outer

def fun(a,b):
    #time.sleep(3)
    print("addition operation1")
    print(a+b)
fun(10,20)
"""
#multiple main function single decorator
"""
import time
def outer(funk):
    def inner(*args,**kwargs):
        print("hello")
        funk(*args,**kwargs)
        print("hi")
    return inner
@outer

def add(a,b):
    time.sleep(3)
    print("addition operation1")
    time.sleep(2)
    print(a+b)
def sub(a,b):
    time.sleep(3)
    print("substraction operation1")
    print(a-b)
def mul(a,b):
    time.sleep(3)
    print("multiplication operation1")
    print(a*b)

add(10,20)
sub(10,20)
mul(1,4)

"""
#write a decorator function calculate executiomn time of a program
"""
import time
def outer(funk):
    def inner(*args,**kwargs):
        start=time.time()
        funk()
        end=time.time()
        difference=end-start
        print(difference)
    return inner
@outer


def fun():
    time.sleep(2)
    print("hi")
fun()

"""
# wap before excuting main function we want to print the main functi9on name
"""
def outer(funk):
    def inner(a,b):
        print(f"calling outer function :{funk.__name__}")
        c=a+b
        if c%2==0:
            print(f" {c} is even")
        else:
            print(f"{c} is odd")
        funk(a,b)
    return inner
@outer    

def add(a,b):
    return a+b
    #print(c)
    #return c
add(1,4) 
"""
#by using multiple decorator single main function
"""
def outer(funk):
    def inner():
        print("qspider")
        funk()
    return inner
def ourtmost(fun):
    def innnermost():
        print("pyspider")
        fun()
    return innnermost
@outer
@ourtmost



def welcome():
    print("welcome to python session")
welcome()
"""
# wap to craeate a decorator to whicvh print the the of the called function along with it sholud 
#check if the number is even or odd
"""
def outer(funk):
    def inner(a):
        print(f"calling function :{funk.__name__}")
        if a%2==0:
            print(f"{a} is even number")
        else:
            print(f"{a} is odd number")
        funk(a)
    return inner
@outer


def check(a):
    #print(a)
    return a
check(11)

"""

# create a de corater to return only positive output from any substraction
"""
def outer(funk):
    def inner(a,b):
        if a-b<0:
            print(abs(a-b))
        funk(a,b)
    return inner
@outer
def sub(a,b):
    c=a-b
    print(c)
    #return c
sub(1,3)
"""
#just for practise
"""
import time
def outermost(fun):
    def wrapping(a,b):
        start=time.time()
        print(a+b)
        fun(a,b)
        end=time.time()
        difference=end-start
        print(difference)
    return wrapping


def outer(funk):
    def inner(a,b):
        time.sleep(5)

        if a-b<0:
            print(abs(a-b))
        time.sleep(3)
        funk(a,b)
    return inner
@outer
@outermost
def sub(a,b):
    time.sleep(3)
    c=a-b

    #print(c)
    #return c
sub(1,3)

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
            time.sleep(n)
            print(m)
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
#1.write a decorator function that prints "HELLO EVERYONE" message
#  before execute any function
#wap to check the role of the person if the role is admoin it should print 
#the username and pass if emp acess denayed if not both it print invalid role

#role 
#func
#if role==admin
#print(acess gtanted)
#elif role==emp
#acess denayed
#print invalid role
#func
"""
def outermost(role):
    def outer(func):

        def innner(*args,**kwargs):
            if role=="admin":
                print("acess granted")
                uname,pwd = func(*args,**kwargs)
                print(f'username={uname} \n password = {pwd}')
            elif role=="emp":
                print("acesss denayed")
            else:
                print("invalid output")
            func(*args,**kwargs)
        return innner
    return outer


@outermost("admin")
def admin():
    username="admin"
    password="admin@123"
    return username,password
# def emp():
#     print("acesss denayed")
admin()
# emp()
"""

#map and filters
"""
x=[1,2,3,4,5,6]
a=lambda i:  i%2==0
print(list(map(a,x)))
print(list(filter(a,x)))
"""

#wap to create a list of 1st characters from each name
"""
names=["manu","lohit","jivago","wank","yaseen"]
fun=lambda i:i[0]
print(list(map(fun ,names)))
"""
#wap to return list of name and length pair
"""
names1=["laptop","mouse","board","house","week"]

fun=lambda i:(i,len(i))
print(list(map(fun,names1)))
"""
#wap to print sum of indices from both list
"""
l1=[2,3,4,5,6]
l2=[3,4,5,8,9]
fun=lambda i,j:i+j
print(list(map(fun,l1,l2)))
 """
#wap to make a pair of names and age
"""
names=["a","b","c","d"]
age=[20,35,21,56]
fun=lambda x,y:(x,y)
print(dict(map(fun,names,age)))
"""
#wap to return if the key is individual returns its value else return its type
"""
d={10:"ten","hai":"value",(1,2,3):"colln",1.2:"decimal"}
fun=lambda i:d.get(i)if isinstance(i,(int,float,complex,bool)) else type(i)
print(list(map(fun,d)))
"""

#1.wap to return a list having only even values
"""
l=[4,3,5,6,7,8,10]
fun=lambda i:i%2==0
print(list(filter(fun,l)))
"""
#2.wap to return a list having only flowers

"""
l=["sun flowers","banana tree","lily flowers","lotus flowers","marigold flowers"]

fun=lambda i:  "flowers" in i
print(list(filter(fun,l)))
"""

#3.wap to return a list having elements which are starting with consonants

"""
l=["hello","guys","please","respond","to","insta","computer"]
fun=lambda i:i[0] not in "aeiou"
print(list(filter(fun,l)))
"""
#4.waf to build a list with only even length strings using filter

"""
k=["apple","google","walmart","fb","insta","act","zomato"]
fun=lambda i:len(i)%2==0
print(list(filter(fun,k)))
"""

#5.waf to return only positive values in the list using filter
"""
m=[-5,-6,9,-34,90,-28,78,100,89,45,-65]
fun=lambda i:i>0
print(list(filter(fun,m)))
"""










