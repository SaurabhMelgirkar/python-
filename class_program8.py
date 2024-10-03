"""
#1
e=[]
o=[]
start=1
while start<=20:
    if start%2==0:
        e.append(start)
        start=start+1
    else:
        o.append(start)
        start=start+1
print(e)
print(o)
"""
"""
#2 -no
l=[1,2,17,49,50]
sum=0
i=0
while i<len(l):
    sum=sum+l[1]
    i=i+1
print(sum)
"""
"""
#3
start=ord("A") 
start2=ord("a")
while start <=ord("Z") and start2<= ord("z"):
    print(chr(start ),chr (start2),end=" ")
    start+=1
    start2+=1
    """
"""
#4
a="hello python"
i=0
while i<=len(a)-1:
    print(a[i],i)
    
    i+=2
    """
"""
#5
x=[1,2,34,[1,2,3],"hi",2+2j,37,True]
i=0
sum=0
while i <len(x)-1:
    if isinstance(x[i],(int,bool,float,complex)):
     print(x[i])
     sum=sum+x[i]
    i=i+1
print(sum)
"""
"""
x=[1,3+8j,"python",[1,2,3],{1,2,3},{7:9}]
i=0
while i<=len(x)-1:
    if isinstance(x[i],list):
        y=x.pop(3)
        z=(x+y)
        print(z)
    i=i+1
    """
"""
y="hello123"
i=0
while i<len(y):
    y[i] in  "aeiou" or y[i].isdigit():
    print(y[i])
    i=i+1
    """

""""
# list comprission

x=[1,2,3,4,5,6]
y=[i**2 for i in x ]
print(y)
"""
"""
x=[1,2,3,4,5,6]
y=[i for i in x if i%2==0]
print(y)
"""
"""
x=[1,2,3,4,5,6]
y=[i if i%2==0 else i**3 for i in x]
print(y)
"""
#set comprission
"""
x=[1,2,3,4,5,6]
y={i**2 for i in x }
print(y)
"""
"""
x=[1,2,3,4,5,6]
y={i for i in x if i%2==0}
print(y)
"""
"""
x=[1,2,3,4,5,6]
y={i if i%2==0 else i**3 for i in x}
print(y)
"""
#tuple generator expression
"""
x=[1,2,3,4,5,6]
y=(i if i%2==0 else i**3 for i in x)
print(tuple(y))
"""
#dictionary 
"""
x=[1,2,3,4,5,6,97]
y={i:chr(i) for i in x}
print(y)
"""
"""
x={1:'A',2:'a',3:'B',4:'b',5:'C',6:'c'}
y={i:i for i in x if i%2==0}
print(y)
"""
"""
l=[2,32,1,52,31,24,56,75]
y=[i for i in l if i%2==0]
print(y)
"""
"""
#2
l=[2,3,5,1,7,2,3]
y=[i**2 if i%2==0 else i**3 for i in l ]
print(y)
"""
"""
#3
l=[i*2 for i in range(1,11) ]
print(l)
"""
"""""
#4
n=int(input("enter number"))
l=[i*n for i in range(1,11) ]
print(l)
"""
#5
"""
l=list(input("enter list"))
m=list(input("enter list no 2"))
n=[]
n=l+m
print(n)
"""
"""
l=eval(input("enter list"))
m=eval(input("enter list no 2"))
x=[sum(i) for i in zip(l,m)]
print(x)
"""
"""
l=["hey","hello","good","evening","python"]
y=[i for i in enumerate(l)]
print(y)
"""
#FUNCTION
"""
def wish():
    print("good morning")
wish()
wish()
wish()
"""
"""
def wish():
    print("good morning")
print(wish)
"""
"""
def addition():
    a=10
    b=20
    print(f"result:{a+b}")
addition()
"""
"""
def palindrome():
    name=eval(input("enter string"))
    if name==name[::-1]:
        print(f"{name} is palindrome]")
    else:
        print(f"{name} is not palindrome]")

palindrome()
"""
"""
def addition():
    a=10
    b=20
    return a+b
res=addition()
print(res)
print(addition())
"""
#variable length argument
"""
def add(*number):
    a=sum(number)
    return a
numbers=add(10,20,40)
print(numbers)
"""
"""
def add(*number):
    print(sum(number))
add(12,34)
add(10,30,40)
"""
#keyword arguments
"""
def info(*num,**info):
    for i,j in info.items():
        print(i,j,num)
info(1,2,name="saurabh",age="21")
info(1,2,name="rahul",age="21")
"""
"""
#add() got some positional-only arguments passed as keyword arguments: 'b'
def add(a,b,/):
    print(a+b)
add(110,b=20)
"""
"""
#add() takes 0 positional arguments but 1 positional argument (and 1 keyword-only argument) were
def add(*,a,b):
    print(a+b)
add(110,b=20) #add(a=110,b=20)
"""
"""
# 4.combination of positional only and keyword only argument:
def add(a,b,/,*,c,d):
    print(a+b+c+d)
add(10,20,c=20,d=40)
"""
"""
def wish(*args):

    print(*args)
 
wish("ge","gn","gm") 
"""
"""
s = "hai"
def char(a,b,c):        #a='h', b='a' c='i'
    print(a,b,c)
char(*s)        
"""
"""

l = [10, 20, 30,40]
def list_sum(*n):          
    print(sum(n))             
list_sum(*l)
"""
#local variable
"""
def fun2(n1, n2):    #n1, n2   are local variable
    print(n1+n2)
    return n1,n2

fun2(30, 20)
#print(n1+n2)
"""
"""
num = 100 
    #global variable
def fun2():
     name ="rohan"
     global num=300     #local variable
     print(num)         #100     #accessing global variable inside the function
     print(name)        #global
fun2()

print(num) 
"""
"""
name="saurabh"
def value_():
    global name      
    name="rohan"
    print(name)

value_()
print( name)
"""
#non local
"""
x=25
def foo1():
    x=10
    def foo():
        nonlocal x
        y=x+5
        print(f"inside {x}")
        print(f"inside {y}")
        #print(y)
    foo()
    print(f"outside {x}")
    
foo1()
print(x)
"""
"""""
def _test():
     n = 10       #non-local variable    #local variable  for test() ,      global variable  for spam()
     def spam():
         m = 20      #local variable for spam()
         print(m)        #20
         print(n)        #10
     spam()
_test()
"""
"""  
#1
def cal(a,b):
    if a>b:
      print(f"sum is {a+b}")
      return a,b
    else:
       print(f"substraction is {a-b}")
       return a,b
cal(6,8)
"""
"""
#2
def palindrome():
 name=input("enter a name")
 if name==name[::-1]:
  print(f"{name} is palindrome")
 else:
  print(f"{name} is not palindrome")
palindrome()
palindrome()
"""
#3
"""
def fun(**name):
   print(len(name))

fun(name1="saurabh",name2="raju")
"""
"""
def fun(*,name="saurabh"):
   print(len(name))

fun()  
"""
"""
#4
def fun(*name):
   print(len(name))

fun("saurabh","raju")
"""
"""
#5
def fun(string,char):
 l=[]
 #string="coding part is done"
 for i,j in enumerate(string):
    if j==char:
      l.append((j,i))
 print(l)
fun("coding part is done","p")
"""


"""
#6
def squre():
 l=[1,2,3,4,5]
 for i in l:
  print(i**2, end=" ")
squre()
"""
"""
#7
def last_digit():
  a=int(input("enter the number"))
  a=str(a)
  for i in a:
    print(a[-1])
    break
last_digit()

"""
"""
#8
def cal():
    a=int(input("enter no 1"))
    b=int(input("enter no 2"))
    c=int(input("enter number 3"))
    addition=a+b
    sub=addition-c
    print(f"addition of first two numbers is {addition} ")
    print(f"substraction  is {sub} ")
cal()
"""
"""
#9
import math as m
def squre(a):
    print(a*a)
def cube(a):
    print(a**3)
def squre_root(a):
    print(m.sqrt(a))
def cube_root(a):
   b = m.pow(a, 1/3)
   print(f"Cubic root of {a} is {round(b, 4)}")
cube_root(8)
squre(2)
squre_root(12)
cube(3)
"""
"""
#10
def check():
    n=input("enter the data")
    if n.isdigit():
        print(f"{n} is digit")
    elif n.isalpha():
        print(f"{n} is alphabate")
    else:
        print(f"{n} is a special character")
check()
check()
check()
"""
"""
#11
def check():
    a=eval(input("enter data"))
    if isinstance(a,(str,tuple,list)):
        print(list(reversed(a)))
    else:
        extra=eval(input("enter exta element"))
        if isinstance(a,set):
          b=a|extra
          print(b)
check()
"""
"""
#12
def func(a,b):
    output=a[b::2]
    return output
print(func("TRACXN",1))
"""
"""
#13
def fun(a,b):
    output=(a[b::2])
    return output
print(fun("TRACXN",0))
"""
"""
#14.A function take variable number of positional arguments
# as input. how to check if the arguments are more than 5. 
def fun(*num):
    
    if len(num)>5:
        print(f"length of {num} is greater than 5 ")
    else:
        print(f"{num}")
fun(1,2,3,4,5,6) 
"""
"""
#15.WAF to reverse any iterable without using reverse function
def fun():
 a=eval(input("enter data"))
 print(str(a)[::-1])

fun()
"""
#16

"""
def fun():
    a=input("enter the string")
    d={}
    for i in a:
        d[i]=ord(i)
    print(d)
fun()
"""
"""
#
#17.waf to reverse a iterable if you are passing string or list or tuple else print type of the data
#def fun():

def fun():
    n=eval(input("enter data"))
    if isinstance(n,(list,tuple,str)):
        print(n[::-1])
    else:
        print(type(n))
fun()
"""
