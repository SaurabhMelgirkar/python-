# CLASS AND OBJECT
"""
class Room:
    trainer="prabhu"
    student_count=34
    subject="python"

r=Room()

print(r.student_count)
print(r.trainer)
print(r.subject)

print(Room.subject)


print(r)
print(Room)
print(Room())
print(id(r))
print(id(Room))
"""
""""

class demo:
    a="hari"
    b=20

d=demo()
d1=demo()
"""
#modificatiom in main class
"""
demo.a="saurabh"
print(d.a)
print(demo.a)
print(d1.a)
d1.a="ankit"
print(d.a)
print(demo.a)
print(d1.a)
"""
"""
#modificaTION IN OBJECT
d.a=100
print(demo.a)
print(d.a)
print(d1.a)

#modificATION IN modified object it does not affect to main class or other object
demo.a=200
print(demo.a)
print(d.a)
print(d1.a)
"""
"""

class test:
    def spam(self):
        print("spaming")
        print(self)
t=test()
print(t)
t.spam()
test.spam(t)
"""
"""
class emp:
    def sal(self):
     amount=1000
     print(f"my total salery is  {amount}")
e=emp()
e.sal()
emp.sal(e)
"""
"""  
class emp:
    def sal(self,amount):
        print(f"total salery is amount {amount}")
e=emp()
e.sal(1000)
emp.sal(e,1000)       
"""
"""
class demo :
    def spam(self,sal):
        if sal==sal[::-1]:
            return sal,True
        else :
            return sal,False
e=demo()
a=e.spam("nayan")
print(a)
"""
"""
class Amazon:
    pname="watch"
    price=550
    cname="sunny"
    cadd="pune"
    
    def order(self):
        print(f"my product name is {self.pname} and price is {self.price} and cusdtomer nane is {self.cname} and adddress is {self.cadd}")
a=Amazon()
a.order()
"""
"""

WAqd to accept list from user when the method is called , forst index element in the list if it is 
string then reverse it then replace in same position and return , else if it is an int then ask for UserWarningto add 
an element into list and return updated list else reverse the list and return
"""
"""

class datatype:
    #n=eval(input("enter list"))
    
    def check(self):
     n=eval(input("enter list"))
    
     if isinstance(n[1],str):
        n[1]=n[1][::-1]
        print(n)
        #return n
     elif isinstance (n[1],int):
            e=eval(input("enter the sting to append"))
            n.append(e)
            print(n)
            #return n
     else :
         print(n[::-1])
         #return n[::-1]

x=datatype()
#print(x.check([1,'hello',(11,3)]))
#x.check([1,"xyz",(23),"saurabh"])    
x.check()

"""
"""
class election:
    date="17/07/2024"
    @classmethod
    def area1(cls):
        print(f"election date is {cls.date}")
    @classmethod
    def area2(cls):
        x=cls()
        x.date="15/07/2024"
        print(f"election date is {x.date}")
    @classmethod
    def area3(cls):
        print(f"election date is {cls.date}")
e=election()
election.date="12/03/2024"
e.area1()
e.area2()
e.area3()
"""
"""
class test:
    a=200
    b=100
    @staticmethod
    def add(a,b):
        return a+b
    @staticmethod
    def sub (a,b):
        return a-b
t=test()
t.a=23
t.b=32
print(t.add(test.a,test.b))
"""
"""
class gym:
    treadmill="25km"
    @classmethod
    def men(cls):
        print(f"total weignt is {cls.treadmill}")
    @staticmethod
    def women(o):
        print(f"total weight {o.treadmill}")
        print(o)
g=gym()
print(g)
#print(o)
gym.treadmill="13 km"
g.men()
g.women(g)
"""
"""
class student:
    def __init__(self):
        print(f"day 1 class")
x=student()
#student __init__(x)
        """
"""
class test:
    def __init__(self):
        print("hi")
    def spam(self):
        print("spam")
t=test()
t.spam()
test.__init__(t)
test.spam(t)
"""
"""
class student:
    def __init__(self):
        print(f"day 1 class")
    def __init__(self):
        print("day 2 class ")
x=student()
student.__init__(x)
"""
#default constructor
"""
class animal:
    def animal_(self):
        print("welcome to zoo")
a=animal()
a.animal_()
"""
#without parameter
"""
class student:
    def __init__(self):
        print(f"welcome to session")
    def person(self):
        print(f"person 1")
s=student()
s.person()
        """
"""
class bank:
    def __init__(self):
        acc_no=12345
        cname="saurabh"
        ifsc="sbi124567"
        branch="pune"
        print( f" my account number is {acc_no} and customer name is {cname} and ifsc code is {ifsc} and branch is {branch}")
b=bank()
b1=bank()
"""
"""
class bank:
    def __init__(self,acc_no,cname,ifsc,branch):
        acc_no=acc_no
        cname=cname
        ifsc=ifsc
        branch=branch
        print( f" my account number is {acc_no} and customer name is {cname} and ifsc code is {ifsc} and branch is {branch}")
b=bank(1234,"saurabh","sbi3456", "pune")
b1=bank(345,"raju","kk234566","nanded")

"""
"""
class bank:
    def __init__(self) :
        self.bal=0
    def deposite(self,amount):
        self.bal+=amount
        print(f"total balance is {self.bal}")
x=bank()
print(x.bal)
#bank.bal=500
x.bal=500
#print(x.bal)
x.deposite(2000)
"""
"""
class bank:
    def __init__(self):
        self.acc_no=12345
        self.cname="saurabh"
        self.ifsc="sbi124567"
        self.branch="pune"
    def details(self):
            print( f" my account number is {self.acc_no} and customer name is {self.cname} and ifsc code is {self.ifsc} and branch is {self.branch}")
b=bank()
b.details()
"""
"""

class bank:
    def __init__(self,acc_no,cname,ifsc,branch):
        self.acc_no=acc_no
        self.cname=cname
        self.ifsc=ifsc
        self.branch=branch
    def details(self):
            print( f" my account number is {self.acc_no} and customer name is {self.cname} and ifsc code is {self.ifsc} and branch is {self.branch}")
b=bank(1234,"saurabh","sbi3456", "pune")
b1=bank(345,"raju","kk234566","nanded")
b.details()
b1.details()
"""
"""
class test:
    def fun(self,a,b):
        print(a,b)
    def fun(self,a=0,b=0,c=0):
        print(a,b,c)
t=test()

t.fun(1,2)
t.fun(1,2,3)
"""
"""
class test:
    def fun(self,a):
        print(a)
    def fun(self,a,b):
        print(a,b)
t=test()
t.fun(1,2)
"""
#constructor overloading
"""
class test:
    def __init__(self,a):
        print(a)
    def __init__(self,a,b):
        print(a,b)
    def __init__(self,a=0,b=0,c=0):
        print(a,b,c)
t=test(1,2,3)
t=test(1,2)
"""

"""
class car:
    def __init__(self,name,color,**arge):
        print(f"my car name is {name} and color is {color} and price is {arge} no is {arge}")
c=car("bmw","black",price=1000,no= 3456)
"""

# inheritamce
"""
class test:
    name="python"
    def spam (self):
        print("spam method")
class sample:
    def demo(self):
        print("demo method")
        x=test()
        x.spam()
        print(x.name)
s=sample()
s.demo()
"""
"""
class car:
    loc="pune"
    def __init__(self):
        print("car class")
    def m1(self):
        print("m1 method")
class car2:
    def __init__(self):
        
        print("car 2 class")
        self.x=car()
        self.x.m1()
        print(self.x.loc)
c=car2()
"""

"""

class Qspider:
    def __init__(self,name,batch,room_no):
        self.name=name
        self.batch=batch
        self.room_no=room_no
    def student_details(self):
        print(f"name of student is {self.name} ,bach is {self.batch}  and room no is {self.room_no} ")
class pyspider:
    def __init__(self,sub,fee,s_count):
        self.sub=sub
        self.fee=fee
        self.s_count=s_count
        self.q=Qspider("rahul","m2",2)
        self.q.student_details()
        
        
    def stuident(self):
        print(f"pyspider student subject is {self.sub}, total fees is {self.fee} and student count is {self.s_count}")
p=pyspider("python ",33000,25)
p.stuident()
"""

"""
#single level inheritance
class dad:
    def villa(self):
        print("this is villa ")
class son(dad):
    def money(self):
        print("money ")
c=son()
c.money()
c.villa()
"""
#multiple inheritance
"""
class hod:
    def work(self):
        print(" hod you have to manage staff")
class teacher(hod):
    def job(self):
        print(" teachers you have to teach student")
class student(teacher):
    def study(self):
        print(" studentss you have to study well ")
s=student()
s.work()
s.job()
s.study()
"""
# multilevel inheritance
"""
class restorent:
    def food(self):
        print("maske food")
class delivery_boy:
    def deliver_food(self):
        print("deliver food to customer")
class customer(restorent,delivery_boy):
    def get_food(self):
        print("get the food")
c=customer()
c.food()
c.deliver_food()
c.get_food()
"""
#herichical inheritance
"""
class parent:
    money=1000
    def party(self):
        print("party mood on")
        
class son(parent):
    def bike(self):
        print(f"{self.money}")
        print("r15")
class daughter(parent):
    def makeup(self):
        print(f"{self.money}")
        print("makeup bok")
s=son()
s.bike()
d=daughter()
d.makeup()


"""

#mathod chaining
"""
class student:
    def class1(self):
        print("day1")
class student2(student):
    def class1(self):
        super().class1()
        print("day2")
s=student2()
s.class1()   
"""
#constructor chaining
"""
class student:
    def __init__(self):
        print("day1")
class student2(student):
    def __init__(self):
        super().__init__()
        print("day2")
s=student2()
"""
#method overloading
"""
class student:
    def __init__(self,name,loc) :
        self.name=name
        self.loc=loc
class clg(student):
    def __init__(self, clg_name, clg_loc):
        super().__init__(name="saurabh", loc="pune")
        self.clg_name=clg_name
        self.clg_loc=clg_loc
    def details(self):
        print(f"{self.clg_loc},{self.clg_name},{self.name},{self.loc}")
c=clg("qspider","deccan")
c.details()

"""
#function overloading
"""
class student:
    def fun(self,name,loc) :
        self.name=name
        self.loc=loc
class clg(student):
    def fun (self, clg_name, clg_loc):
        super().fun(name="saurabh", loc="pune")
        self.clg_name=clg_name
        self.clg_loc=clg_loc
    def details(self):
        print(f"{self.clg_loc},{self.clg_name},{self.name},{self.loc}")
c=clg()
c.fun("qspider","deccan")
c.details()
"""
#hybrid inheritance
"""
class character:
        def m1(self):
            health=1000
            mana ="mana"
            attack=1500
            print(f"{attack},{health},{mana}")
class specialcaster(character):
    def m2(self):
        print(f" this is special caster class and health is  attack is  and mana is  ")
class melee_fighter(character):
     def special_ablities(self):
         self.melle_attack=2000
         print(f"{self.melle_attack}")
class paladin(specialcaster,melee_fighter):
     def m3(self):
        print(f"this is paladin class")
p=paladin()
p.m1()
p.m2()
p.special_ablities()
p.m3()
"""
"""
class A:
    def spam(self):
        print("spin")
class B:
    def spam(self):
        print("demo")
class C (A,B):
    def cool(self):
        print("spam & demo")
x=C()
#x.cool()
#x.spam()
print(C.__mro__)
"""
"""
class A:
    a=10
    b=15
    print(f"{a} and {b}")
class B:
    b=20
    a=38
    print(f"{a} and {b}")
class C (A,B):
        a=23
        b=34
        c=28
        print(f"{a},{c},{b}")
x=C()
#x.cool()
#x.spam()
print(C.__mro__)
"""

#class inside class 
"""
class A:
    def fun2(self):
        print("a")

    class B:
        def fun2(self):
            print("b")
x=A()
y=x.B()
y.fun2()
x.fun2()
"""
"""
class A:
    def fun(self):
        print("a")

    class A:
        def fun(self):
            print("b")
        class A:
            def fun(self):
                print("c")
x=A()
y=x.A()
z=y.A()
y.fun()
x.fun()
z.fun()
"""
#abstraction 
"""
from abc import ABC ,abstractmethod
class pyspider(ABC):
    @abstractmethod
    def sub1(self):
        pass
    @abstractmethod
    def sub2(self):
        pass
    @abstractmethod
    def sub3(self):
        pass
class Qspider(pyspider):
    def sub1(self):
        print("python")
    def sub2(self):
        print("java")
    def sub3(self):
        print("sql")
q=Qspider()
q.sub1()
q.sub2()
q.sub3()

"""  
"""
from abc import ABC ,abstractmethod
class Bank(ABC):
    @abstractmethod
    def balance(self,amount):
        pass
    @abstractmethod
    def deposite(self,amount):
        pass
    @abstractmethod
    def withdraw(self,amount):
        pass
class Atm(Bank):
    def __init__(self,Bank_name,bal):
        self.Bank_name=Bank_name
        self.bal=bal
    def balance(self):
        print(f"total balance is {self.bal}")
    def deposite(self,amount):
        self.bal+=amount
        print(f"total balance after  deposite is {self.bal}")
    def withdraw(self, amount):
        self.bal-=amount
        print(f" total balance afyer withrow amount is{self.bal}")
a=Atm(Bank_name="sbi",bal=50000)
print(a.Bank_name)
print(a.bal)
a.balance()
a.deposite(10)
a.withdraw(5)
"""
# ticket booking
"""
from abc import ABC , abstractmethod
class theater(ABC):
    @abstractmethod
    def theater_name(self , Theater_name):
        pass
    @abstractmethod
    def counter_number(self,Counter_no):
        pass
    @abstractmethod
    def movie_name(self,Movie_name):
        pass
    @abstractmethod
    def no_of_ticket_taken(self,no):
        pass
    @abstractmethod
    def ticket_price(self,ticket_price):
        pass
    @abstractmethod
    def extra_things_taken(self,drink=None,food=None,drink_price=None,food_price=None):
        pass
    @abstractmethod
    def parking_charges(self,charges):
        pass
    @abstractmethod
    def total_bill(self, Total_bill):
        pass

class Movie_lover(theater):
    def theater_name(self , Theater_name):
        self.Theater_name=Theater_name
        print(f"your selected theater name is {self.Theater_name}")
    def movie_name(self,Movie_name):
        self.Movie_name=Movie_name
        print(f"you are selected movie is {self.Movie_name}")
     
    def counter_number(self,Counter_no):
        self.Counter_no=Counter_no
        print(f"to take the ticket of the movie {self.Movie_name} you hane to go to counter no {self.Counter_no}")
    
    def no_of_ticket_taken(self,no):
        self.no=no
        print(f"you bought total {self.no} tickets")
    
    def ticket_price(self,Ticket_price):
        self.Ticket_price=Ticket_price
        print(f"price for the movie {self.Movie_name} for single person is {self.Ticket_price}")
    
    def extra_things_taken(self,drink,food,drink_price,food_price):
        self.food=food
        self.drink=drink
        self.food_price=food_price
        self.drink_price=drink_price
        if food!=None:
            print(f"you bought  food is {self.food} and price of that food is {self.food_price}")
        
        if drink!=None:
          print(f"you bought  drink is {self.drink} and price of that drink is {self.drink_price}")
    
    
    def parking_charges(self,charges):
        self.charges=charges
        print(f"parking charges is {self.charges}")
    
    def total_bill(self, Total_bill):
        self.t=self.Ticket_price * self.no
        self.Total_bill=Total_bill +self.charges+self.food_price+self.drink_price + self.t
        print(f"your total bill is rs {self.Total_bill}")
        print("\n           Thank you                  ")
      
m=Movie_lover()
m.theater_name("PVR")
m.movie_name("kalaki ")
m.counter_number(2)
m.no_of_ticket_taken(5)
m.ticket_price(200)
m.extra_things_taken(food="pizza",food_price=1000, drink="coke",drink_price=300)
m.parking_charges(100)
m.total_bill(0)

"""

#encapsulation
"""
class details:
    def __init__(self,name,_loc,__id):
        self.name=name
        self._loc=_loc
        self.__id=__id
        print(self.name,self.__id,self._loc)
d=details("saurabh","pune",1012)
    
"""
"""
class Atm:
    _pin=123
    def bank(self):
        print(f"{self._pin}")
a=Atm()
a.bank()
a._pin=1000
print(a._pin)
#1print(a.Atm._pin)
a.bank()
"""

#accesssing private variable in childd class
"""
class dad:
    __name="sudhir"
    def spam(self):
        print(f"my dad name is {self.__name}")
class son(dad):
    def demo(self):
        print(f"demo method and {self.spam()}")
a=son()
a.demo()
a.spam()
"""
"""
class dad:
    _name="sudhir"
    def spam(self):
        print(f"my dad name is {self._name}")
class son(dad):
    def demo(self):
        print(f"demo method and {self._name}")
a=son()
a.demo()
a.spam()

"""
#getter setter and detelter method
"""
class bank:
    def __init__(self,name):
        self.name=name
    def getting(self):
        print("getting the name")
        return self.name
    def setting(self,name):
        print(f"setting the name ")
        self.name=name
    def deleting(self):
        del self.name
b=bank("vikas")
print(b.getting())
b.setting("saurabh")
print(b.getting()) 
b.deleting()
"""
    



