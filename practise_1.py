#Square and Cube: Create a lambda function to square and cube each number in a given list of integers.
"""
l=[2,4,6,8,9]
x=lambda l:[ i**3 for i in l]
y=lambda l:[ i**2 for i in l]
print(x(l))
print(y(l))
"""
"""
x=lambda l:f"{l} is palendrome" if str(l)==str(l)[::-1] else f"{l} is not palendrome"
print(x(111))
"""
"""
s="saurabh"
x=lambda l:f"{s} starts with {l} character" if s[0]==l else f" {s} it is not  starting with {l} character"
print(x("s"))
"""
"""
l=[1,5,7,8,9]
x=lambda i:[ i%2==0  for i in l ]   
print(x(l))
"""
"""
l=[1,5,7,8,9]
for i in l:
    if i%2==0:
        print(i)

"""
"""
t=[1,3,6,5]
for i in range(0,len(t)):
    for j in range(i+1,len(t)):
        if t[i]>=t[j]:
            t[i],t[j]=t[j],t[i]
print(tuple(t))
"""
"""
t=[1,3,6,5]
x=lambda i:[i for i in range(0,len(t))]
print(x(t))
"""
"""
l=["s","a","u"]
x=lambda i:[i*2 for i in l]
print(x(l))
"""
"""
a= int(input("enter the number"))
fact=1
for i in range(1,a+1):
    fact=fact*i
print(fact)
"""
"""
a= int(input("enter the number"))
fact=1
x=lambda a:[f"{fact*i}" for i in range(1,a+1) ]
print(x(a))
"""
#instance mathod (modification can be done with class name as well as object)
"""
class demo:
    ""hi this is program ""
    a=10
    def fun(self):
        print(self.a)
        print(self)
       # print(demo.__dict__)
d=demo()
#d.a=20
d.fun()
demo.a=45
demo.fun(d)
#print(help(demo))
print(demo.__doc__)
print(d)
"""

#class method (modification done with only class name not with object)
"""
class Demo:
    a=10
    b="saurabh"
    @classmethod
    def fun(cls):
        print(cls.a)
        print(cls.b)
        print(cls)
d=Demo()
Demo.a=20
d.fun()
print(d)
"""
#static method(we cant do modification with class name or object)
"""
class Demo:
    a=10
    @staticmethod
    def fun():
        b=30
        print(Demo.a)
        print(b)
d=Demo()
Demo.a=20
Demo.b=40 
d.fun()
print(Demo)
print(d)
"""
# method overloading
"""
class demo:
    def fun(self,a):
        print(a)
    def fun(self,a,b):
        print(a+b)
    def fun(self,a=0,b=0,c=0):
        print(a+b+c)
d=demo()
d.fun(1,4,5)
"""
#constructor overloading
"""
class demo:
    def __init__(self,a):
        print(a)
    def __init__(self,a,b):
        print(a+b)
    def __init__(self,a=0,b=0,c=0):
        print(a+b+c)
d=demo(1,2)
d=demo(1,2,3)
"""
#has reletionship
"""
class Demo:
    b="saurabh"
    def __init__(self):
        self.a=10
        
    def fun1(self):
        print("hi")
class Demo2:
    def __init__(self):
        print("its in class 2")
        self.x=Demo()
        print(self.x.a)
        print(self.x.b)
        self.x.fun1()
    def fun2(self):
        print("i am in")
d=Demo2()
d.fun2()
"""

#inheritance single level
"""
class Animal:
    name=input("enter the name of animal")
    print(name)
    def __init__(self,owner):
        self.owner=owner
        print(self.owner)
    def details(self):
        print(self.owner , self.name)
       
class home(Animal):
    def adress(self,add):
        print(add)
h=home("saurabh")
h.details()
h.adress("pune")
"""
#multi level inheritance
"""
class grandfather:
    def home(self):
        print(" i have home")
class father (grandfather):
    def car(self):
        print(f"i have car and home")
class son (father):
    def bike(self):
        print(f"i have car , home and bike")
c=son()
c.home()
c.bike()
c.car()
"""
#multiple inheritabce (multiple parent 1 child)
"""
class parent1:
    def gold(self):
        print("i have 10 kg gold")
class parent2:
    def silver(self):
        print("1 kg silver")
class son(parent1,parent2):
    def nothing(self):
        print("nothing")
s=son()
s.nothing()
s.gold()
s.silver()
"""
#herichical inheritance (multiple childs 1 parent)
"""
class parent1:
    def amount1(self,amount):
        self.amount=amount
        print(amount)
class son(parent1):
    def bike(self):
        print(f"i want your amount {self.amount} for purchasing bike")
class daughter(parent1):
    def makeupkit(self):
        print(f"i want your amount {self.amount} for purchasing makeup kit ")
c=son()
c.amount1(1000)
c.bike()
g=daughter()
g.amount1(1200)
g.makeupkit()


"""
#hybrid inheritance
"""
class grandpa:
    def fun(self):
        print("grand pa")
class father(grandpa):
    def fun(self):
         super().fun()
         print("father")
class Mother(grandpa):
    def fun(self):
        super().fun()
        print("mother")
class child(Mother,father):
    def fun(self):
        super().fun()
        print("chold")
c=child()
c.fun()
"""
#happy number
"""
num=230
no=num
while num>1:
    rem=num%10
    rem2=num//10
    rem3=rem2%10
    rem4=rem2//10
    #rem3=rem//10
    #print(rem,rem2,rem3)
    mul=rem **2 + rem3**2 +rem4**2
    print(mul)
    num=mul
    #break
if mul%10==1 :
    print(f"{no} is happy number")
else:
    while num>0:
            r=num%10
            r2=num//10
            r3=r2%10
            r4=r2//10

            mul=r **2 + r3**2 +r4**2
            num=mul
            print(num)
""" 
#trying except block              
"""
else:
    try:
        while num>0:
            r=num%10
            r2=num//10
            r3=r2%10
            r4=r2//10

            mul=r **2 + r3**2 +r4**2
            num=mul
            print(num)
    except:
        print(f"{no } is not happy number")
"""    
            

        

#abstarct method
"""
from abc import ABC ,abstractmethod
class demo(ABC):
    @abstractmethod
    def sum(self,a,b):#---abstract method
        pass
    def sub(self,a,b):#--- concret method
        print(f"sub is {a-b}")
class Test(demo):
    def sum(self,a,b):
        print(f"sum is {a+b}")
t=Test()
t.sum(2,4)
t.sub(4,2)
"""
#getter setter method
"""
class bank:
    def __init__(self,name):#-----def fun(self,name)
        self.name=name
    def getting(self):
        print("getting the name")
        return self.name
    def setting (self,name):
        print("setting name")
        self.name=name
    def deleter(self):
        del self.name
b=bank("saurabh")
 #----b.fun("saurabh")
print(b.getting())
b.setting("raju")
print(b.getting())   
b.deleter()  
#print(b.getting()) bank has no attribute name due to deletter   
"""
#combination of all inheritance concepts 
"""

Question:

Design a simple zoo management system in Python that demonstrates the following concepts:

Abstraction: Create an abstract base class named Animal with abstract methods for make_sound and eat.
Encapsulation: Ensure that the properties of Animal (such as name and age) are private and provide public getter and setter methods to access them.
Inheritance: Derive two classes, Lion and Parrot, from Animal. Each class should implement the abstract methods in a way that reflects the specific behavior of each animal (e.g., Lion might roar and Parrot might squawk).
Polymorphism: Implement a method in your main program that accepts a list of Animal objects and calls the make_sound and eat methods on each item in the list, demonstrating how different animals can exhibit different behaviors.
Write the Python code for these classes and methods, and provide an example of how you would use them in a sample application to demonstrate these concepts.


"""
#Answer of the given question

"""
from abc import ABC ,abstractmethod
class Animal(ABC):
    def name(self,name,age):
        self.__name=name
        self.__age=age
    def getting(self):
        #print("getting name and age")
        return self.__name,self.__age
    def setting(self,name,age):
        #print("setting name and age")
        self.__name=name
        self.__age=age
    @abstractmethod
    def sound(self,sound):
        pass
    def eat(self,eat):
        pass
class Lion(Animal):
    
    def sound(self, sound):
        super().sound(sound)
        print(f"sound is {sound}")
    def eat(self, eat):
         super().eat(eat)
         print(f"eatting {eat}")

class Parrot(Animal):
    def sound(self, sound):
        super().sound(sound)
        print(f"sound is {sound}")
    def eat(self, eat):
         super().eat(eat)
         print(f"eatting {eat}")
a=Lion()
print("lion details")
print(" ")
a.name(name="lion",age=23)
print(a.getting())
a.setting(name="lion",age=34)
print(a.getting())
a.sound("roar")
a.eat("meat")

print(" ")
print("parrot details ")
print(" ")
a=Parrot()
a.name(name="parrot",age=23)
print(a.getting())
a.setting(name="Parrot",age=34)
print(a.getting())
a.sound("squawk")
a.eat("chilly")

"""

#1.WAP to find the length of the string without using inbuilt funct.
"""
s="hello python"
#print(len(s))
count=0
for i in s:
    count=count+1
print(count)
"""
# #2.WAP to reverse a string without using inbuilt function
"""
s = 'hello pyhton'
print(s[::-1]) 
"""
# #3. WAP to replace one string with another. # 
# #eg: hello world---> hello Universe.
"""
s = 'Hello World'
u = 'Universe'

re=s.replace('World',u)
print(re)

r=""
for i in s.split():
    if i=="World":
        r=r+ " "+u
    else:
        r=i+' '
print(r)
"""
# #4.WAP to convert string into list and vice versa.
s = 'hello world'
"""
if isinstance(s,str):
    print(list(s))
elif isinstance(s,list):
    print(str(s))
else:
    print("it is not a string as well as list") 
    """
#logic 2
"""
print(s.split())
print(''.join(s.split()))
l = []
st = ''
for i in s:
    if i != ' ':
        st += i
    else:
        l += [st]
        st = '' 
        l += [st]
print(l)
"""
#logic 3
# #Another way string to list
# for i in s:
# l += [i]
# print(l)
#
# #converting from list to string
# for i in l:
# st += i
#
# print(st)
#Square and Cube: Create a lambda function to square and cube each number in a given list of integers.
"""
l=[2,4,6,8,9]
x=lambda l:[ i**3 for i in l]
y=lambda l:[ i**2 for i in l]
print(x(l))
print(y(l))
"""
"""
x=lambda l:f"{l} is palendrome" if str(l)==str(l)[::-1] else f"{l} is not palendrome"
print(x(111))
"""
"""
s="saurabh"
x=lambda l:f"{s} starts with {l} character" if s[0]==l else f" {s} it is not  starting with {l} character"
print(x("s"))
"""
"""
l=[1,5,7,8,9]
x=lambda i:[ i%2==0  for i in l ]   
print(x(l))
"""
"""
l=[1,5,7,8,9]
for i in l:
    if i%2==0:
        print(i)

"""
"""
t=[1,3,6,5]
for i in range(0,len(t)):
    for j in range(i+1,len(t)):
        if t[i]>=t[j]:
            t[i],t[j]=t[j],t[i]
print(tuple(t))
"""
"""
t=[1,3,6,5]
x=lambda i:[i for i in range(0,len(t))]
print(x(t))
"""
"""
l=["s","a","u"]
x=lambda i:[i*2 for i in l]
print(x(l))
"""
"""
a= int(input("enter the number"))
fact=1
for i in range(1,a+1):
    fact=fact*i
print(fact)
"""
"""
a= int(input("enter the number"))
fact=1
x=lambda a:[f"{fact*i}" for i in range(1,a+1) ]
print(x(a))
"""
#instance mathod (modification can be done with class name as well as object)
"""
class demo:
    ""hi this is program ""
    a=10
    def fun(self):
        print(self.a)
        print(self)
       # print(demo.__dict__)
d=demo()
#d.a=20
d.fun()
demo.a=45
demo.fun(d)
#print(help(demo))
print(demo.__doc__)
print(d)
"""

#class method (modification done with only class name not with object)
"""
class Demo:
    a=10
    b="saurabh"
    @classmethod
    def fun(cls):
        print(cls.a)
        print(cls.b)
        print(cls)
d=Demo()
Demo.a=20
d.fun()
print(d)
"""
#static method(we cant do modification with class name or object)
"""
class Demo:
    a=10
    @staticmethod
    def fun():
        b=30
        print(Demo.a)
        print(b)
d=Demo()
Demo.a=20
Demo.b=40 
d.fun()
print(Demo)
print(d)
"""
# method overloading
"""
class demo:
    def fun(self,a):
        print(a)
    def fun(self,a,b):
        print(a+b)
    def fun(self,a=0,b=0,c=0):
        print(a+b+c)
d=demo()
d.fun(1,4,5)
"""
#constructor overloading
"""
class demo:
    def __init__(self,a):
        print(a)
    def __init__(self,a,b):
        print(a+b)
    def __init__(self,a=0,b=0,c=0):
        print(a+b+c)
d=demo(1,2)
d=demo(1,2,3)
"""
#has reletionship
"""
class Demo:
    b="saurabh"
    def __init__(self):
        self.a=10
        
    def fun1(self):
        print("hi")
class Demo2:
    def __init__(self):
        print("its in class 2")
        self.x=Demo()
        print(self.x.a)
        print(self.x.b)
        self.x.fun1()
    def fun2(self):
        print("i am in")
d=Demo2()
d.fun2()
"""

#inheritance single level
"""
class Animal:
    name=input("enter the name of animal")
    print(name)
    def __init__(self,owner):
        self.owner=owner
        print(self.owner)
    def details(self):
        print(self.owner , self.name)
       
class home(Animal):
    def adress(self,add):
        print(add)
h=home("saurabh")
h.details()
h.adress("pune")
"""
#multi level inheritance
"""
class grandfather:
    def home(self):
        print(" i have home")
class father (grandfather):
    def car(self):
        print(f"i have car and home")
class son (father):
    def bike(self):
        print(f"i have car , home and bike")
c=son()
c.home()
c.bike()
c.car()
"""
#multiple inheritabce (multiple parent 1 child)
"""
class parent1:
    def gold(self):
        print("i have 10 kg gold")
class parent2:
    def silver(self):
        print("1 kg silver")
class son(parent1,parent2):
    def nothing(self):
        print("nothing")
s=son()
s.nothing()
s.gold()
s.silver()
"""
#herichical inheritance (multiple childs 1 parent)
"""
class parent1:
    def amount1(self,amount):
        self.amount=amount
        print(amount)
class son(parent1):
    def bike(self):
        print(f"i want your amount {self.amount} for purchasing bike")
class daughter(parent1):
    def makeupkit(self):
        print(f"i want your amount {self.amount} for purchasing makeup kit ")
c=son()
c.amount1(1000)
c.bike()
g=daughter()
g.amount1(1200)
g.makeupkit()


"""
#hybrid inheritance
"""
class grandpa:
    def fun(self):
        print("grand pa")
class father(grandpa):
    def fun(self):
         super().fun()
         print("father")
class Mother(grandpa):
    def fun(self):
        super().fun()
        print("mother")
class child(Mother,father):
    def fun(self):
        super().fun()
        print("chold")
c=child()
c.fun()
"""
#happy number
"""
num=230
no=num
while num>1:
    rem=num%10
    rem2=num//10
    rem3=rem2%10
    rem4=rem2//10
    #rem3=rem//10
    #print(rem,rem2,rem3)
    mul=rem **2 + rem3**2 +rem4**2
    print(mul)
    num=mul
    #break
if mul%10==1 :
    print(f"{no} is happy number")
else:
    while num>0:
            r=num%10
            r2=num//10
            r3=r2%10
            r4=r2//10

            mul=r **2 + r3**2 +r4**2
            num=mul
            print(num)
""" 
#trying except block              
"""
else:
    try:
        while num>0:
            r=num%10
            r2=num//10
            r3=r2%10
            r4=r2//10

            mul=r **2 + r3**2 +r4**2
            num=mul
            print(num)
    except:
        print(f"{no } is not happy number")
"""    
            

        

#abstarct method
"""
from abc import ABC ,abstractmethod
class demo(ABC):
    @abstractmethod
    def sum(self,a,b):#---abstract method
        pass
    def sub(self,a,b):#--- concret method
        print(f"sub is {a-b}")
class Test(demo):
    def sum(self,a,b):
        print(f"sum is {a+b}")
t=Test()
t.sum(2,4)
t.sub(4,2)
"""
#getter setter method
"""
class bank:
    def __init__(self,name):#-----def fun(self,name)
        self.name=name
    def getting(self):
        print("getting the name")
        return self.name
    def setting (self,name):
        print("setting name")
        self.name=name
    def deleter(self):
        del self.name
b=bank("saurabh")
 #----b.fun("saurabh")
print(b.getting())
b.setting("raju")
print(b.getting())   
b.deleter()  
#print(b.getting()) bank has no attribute name due to deletter   
"""
#combination of all inheritance concepts 
"""

Question:

Design a simple zoo management system in Python that demonstrates the following concepts:

Abstraction: Create an abstract base class named Animal with abstract methods for make_sound and eat.
Encapsulation: Ensure that the properties of Animal (such as name and age) are private and provide public getter and setter methods to access them.
Inheritance: Derive two classes, Lion and Parrot, from Animal. Each class should implement the abstract methods in a way that reflects the specific behavior of each animal (e.g., Lion might roar and Parrot might squawk).
Polymorphism: Implement a method in your main program that accepts a list of Animal objects and calls the make_sound and eat methods on each item in the list, demonstrating how different animals can exhibit different behaviors.
Write the Python code for these classes and methods, and provide an example of how you would use them in a sample application to demonstrate these concepts.


"""
#Answer of the given question

"""
from abc import ABC ,abstractmethod
class Animal(ABC):
    def name(self,name,age):
        self.__name=name
        self.__age=age
    def getting(self):
        #print("getting name and age")
        return self.__name,self.__age
    def setting(self,name,age):
        #print("setting name and age")
        self.__name=name
        self.__age=age
    @abstractmethod
    def sound(self,sound):
        pass
    def eat(self,eat):
        pass
class Lion(Animal):
    
    def sound(self, sound):
        super().sound(sound)
        print(f"sound is {sound}")
    def eat(self, eat):
         super().eat(eat)
         print(f"eatting {eat}")

class Parrot(Animal):
    def sound(self, sound):
        super().sound(sound)
        print(f"sound is {sound}")
    def eat(self, eat):
         super().eat(eat)
         print(f"eatting {eat}")
a=Lion()
print("lion details")
print(" ")
a.name(name="lion",age=23)
print(a.getting())
a.setting(name="lion",age=34)
print(a.getting())
a.sound("roar")
a.eat("meat")

print(" ")
print("parrot details ")
print(" ")
a=Parrot()
a.name(name="parrot",age=23)
print(a.getting())
a.setting(name="Parrot",age=34)
print(a.getting())
a.sound("squawk")
a.eat("chilly")

"""

#1.WAP to find the length of the string without using inbuilt funct.
"""
s="hello python"
#print(len(s))
count=0
for i in s:
    count=count+1
print(count)
"""
# #2.WAP to reverse a string without using inbuilt function
"""
s = 'hello pyhton'
print(s[::-1]) 
"""
# #3. WAP to replace one string with another. # 
# #eg: hello world---> hello Universe.
"""
s = 'Hello World'
u = 'Universe'

re=s.replace('World',u)
print(re)

r=""
for i in s.split():
    if i=="World":
        r=r+ " "+u
    else:
        r=i+' '
print(r)
"""
# #4.WAP to convert string into list and vice versa.
s = 'hello world'
"""
if isinstance(s,str):
    print(list(s))
elif isinstance(s,list):
    print(str(s))
else:
    print("it is not a string as well as list") 
    """
#logic 2
"""
print(s.split())
print(''.join(s.split()))
l = []
st = ''

for i in s:
    if i != ' ':
        st += i
    else:
        l += [st]
        st = '' 
        l += [st]
print(l)
"""
#logic 3
"""

#Another way string to list
for i in s:
     l += [i]
     #print(l)

#converting from list to string
for i in l:
     st += i
print(st)
"""
# #7.WAP to print ascii values of string
"""
s = 'hello python'
d={}
for i in s:
    d[i]=ord(i)
print(d)
"""
# #8.WAF to convert upper case into lower case and vice versa. 
"""
def swap_case(string, s1 =''):
     for i in string:
        if "a"<=i <="z":
            s1+=chr(ord(i)-32)
           
        else:
            s1+=chr(ord(i)+32)
     print(s1)
swap_case("HELLO")



"""
#29.Bank Account management System
#Classes:--> Account, Customer Transaction
#Objects: individual accounts, customers transactions
#Inheritance: Saving saccount, checking Account inherit from Account
#Polymorphism: Deposit, withdraw methods behave differently for each account type
#Encapsulations: Account balance, customer info hidden from external access"""
"""
class customer:
    def __init__(self ,phone, name):
        self._phone=phone
        self._name=name
    def get_info(self):
        return self._name,self._phone
    
class Transiction:
    def __init__(self,amount,date):
        self.amount=amount
        self.date=date
    def get_amount(self):
        return self.amount
    def get_date(self):
        return self.date
    


class Account:
    
    def __init__(self,account_no,balance):
        self.account_no=account_no
        #self.customer=customer
        self.balance=balance
    
    def get_balance(self):
            return self.balance
    
    def get_account_no(self):
        return self.account_no
    
    def deposite(self,amount):
        self.amount=amount
        self.balance+=amount
   
    def withdraw(self,w_amount):
        self.w_amount=self.w_amount
        self.amount-=w_amount
       # raise NotImplementedError("Subclasses must implement withdraw()")
    




class Saving_acc(Account):
    def __init__(self, account_no, balance):
        super().__init__(account_no, balance)
    def withdraw(self, w_amount):
        return super().withdraw(w_amount)

class Checking_acc_balance(Account):
    def __init__(self, account_no, balance):
        super().__init__(account_no, balance)
    def withdraw(self, w_amount):
        return super().withdraw(w_amount)
    
 




c=customer(12345678,"raju")
s=Saving_acc(34666,1000)
s.deposite(500)
print(f"saving account balance{s.get_balance()}")
c2=Checking_acc_balance(234455,1000)
c2.withdraw(700)
print(f"checking account balance{c2.get_balance()}")

    
#class Saving_account(Account):

"""
#am to pm converting
"""
import re
import datetime
from datetime import *
s ='The Python class starts at 7:00 am in the morning and 19:00 pm in the evening'
x=re.findall("\d+:+\d{2}",s)
#y=re.findall("\d{2}\s*[:;]\s*\w\S+",s)
for i in x:
    _24hr = str(i)
    obj = datetime.strptime(_24hr, "%H:%M")
    _12hr = obj.strftime("%I:%M %p")
    print(_12hr) 
"""
#32. WAP to seaprate file names based on extensions

"""
import re
files= ['demo.txt', 'loops.py', 'for loop.py', 'data.xlx', 'pres.ppt', 'spam.txt',
         'document.doc', 'spam.py', 'python.xlx', 'methods.ppt', 'string.ppt',
           '1ist.doc']
d={}
for i in files:     
    x=i.rsplit(".",1)
    if x[1]  not in d:
        d[x[1]]=[x[0]]
    else:
        d[x[1]]+=[x[0]]
print(d)
"""
#33. WAP to check whether the list is containing elements starting with vowels and check whether it is even or odd length
"""
names= ['apple', 'google', 'yahoo', 'ebay', 'ensiion', 'intel', 'capgemini',
            'redbus', 'amazon', 'unisya', 'ust', 'oracle']
vovels=[]
even=[]
odd=[]
con=[]
for i in names:
    if i[0] in "aeiou":
        vovels.append(i)
for j in names:
    if len(j)%2==0 and j[0] in "aeiou":
            even.append(j)
            
    elif len(j)%2==1 and j[0] in "aeiou":
            odd.append(j)
    else:
          con.append(j)
          
d1={"vovels":vovels}
d2={"odd vowels":odd}
d3={"constnents":con}
d={"even vovels ":even}
print(d1)
print(d)
print(d2)
print(d3)

"""
#9 sir questions
# #9.WAP to swap 2 numbers without using third variable
"""
a = 45
b = 76
a=a+b
b=a-b
a=a-b
print(a)
print(b)
"""
# #9.WAP to swap 2 numbers without using third variable
"""
a = 45
b = 76
a,b=b,a
print(b)
print(a)


"""
# #10.WAP to merge two list.
"""
from itertools import zip_longest

l1 = [1,3,5,7]
l2 = [2,4,6,8]
#print(l1+l2)
a=list(zip_longest(l1,l2, fillvalue=0))
print(a)
b=list(zip(l1,l2))
print(b)

"""
# #14.WAP to check given string is Palindrome. # 
"""
s = 'malayalam'
if s[::-1]:
    print(f"{s} is palendrome")
else:
    print(f"{s} is not palendrome")
"""
# #15.WAP to search for the character in a string and return the
# #corresponding index. 
"""
s = 'hello world' 
ch = 'w'
for i in s:
    if i==ch:
        a=s.index(i)
        print(s[a+1])
    else:
       #print("it is not present")
       pass
    """
