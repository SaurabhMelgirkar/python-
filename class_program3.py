"""
#1
s=eval(input("enter data"))
if s.isupper():
    print(f"{s} is in uppercase")
elif s.islower():
    print(f"{s} is in lowercase")

elif s.isdigit():
    print(f"{s} is a digit")

else:
    print("it is special character")
    """
""""
s=eval(input("enter data"))

if ord("A")<=ord(s)<=ord("Z"):
    print("uppercase")
elif ord("a")<=ord(s)<=ord("z"):
    print("lowercase")

elif ord("0")<=ord(s)<=ord("9"):
    print("digit")

else:
    print("special character")
    """

"""
#2
a=eval(input("enter data"))
if isinstance(a,(int,float,bool,complex)):
    print("it is individual data ")
elif isinstance(a,(list,tuple,str)):
    print("it is a sequence data type")
else:
    print("ietrable")
    """
"""
#3
a=eval(input("enter data"))
#b=["1","4","hi",1]
if isinstance(a,str):
    print(len(a))
elif isinstance(a,list):
    a.pop()
    print(a)
elif isinstance(a,tuple):
    print(a[-1: :1])
else:
    print("invalid")
"""
"""""
#4
age=eval(input("enter your age"))
if age>0 and age<17:
    print("child") 
elif age>18 and age<30:
    print("adult")
elif age>30 and age<=60:
    print("men")
elif age>60 and age <=130:
    print("senior citizon")

else:
    print("invalid")
"""
"""
#5
a=int(input("enter your date of joining"))
current_year=2024
exp=current_year-a
print(exp)
if exp>=0 and exp<=2:
 print("no hike")
elif exp>=3 and exp<=5:
   print("hike 5000 rs")
elif exp>=6 and exp<=8:
   print("hike 7000 rs")
elif exp>=9:
   print("hike 10000 rs")

else:
    print("invalid")
"""
"""
#6
a=65
b=34
c=76
if a>b and a>c:
    print(f"{a} is greater than {b} and {c}")
elif b>a and b>c:
    print(f"{b} is greater than {a} and {c}")
elif c>a and c>b:
    print(f"{c} is greater than {a} and {b}")
else:
    print("all are same")



"""
"""
#7
sub1=int(input("enter the marks of sub1 between 1 to 100"))
sub2=int(input("enter the marks of sub2 between 1 to 100"))
sub3=int(input("enter the marks of sub3 between 1 to 100"))
sub4=int(input("enter the marks of sub4 between 1 to 100"))
sub5=int(input("enter the marks of sub5 between 1 to 100"))
av=sub1 + sub2 + sub3 + sub4 + sub5
avg=av/5
if avg>=90 and avg<=100:
    print("Distinction")
elif avg>=75 and avg <=89:
    print("First class")
elif avg>=60 and avg<=74:
    print("second class")
elif avg>=50 and avg<=59:
    print("third class")
else:
    print("fail")

"""
"""
#8
h=eval(input("enter the hight of student"))
Height=[1,]
print(Height)

if h>0:
    Height.append(h)
    print(Height)
    x=Height.sort()
    print(x)
else:
    print("invalid height")

"""
"""
#9
age=int(input("enter the age "))
if age>=0 and age<=12:
    print("you are child")
elif age>=13 and age<21:
    print("you are adult ") 
elif age>=21:
    print("you can marry")
else:
    print("invalid age")
    """
"""
#10
p1=int(input("enter product 1 price"))
p2=int(input("enter product 2 price"))
p3=int(input("enter product 3 price"))
total=p1+p2+p3
print(total)
if total>=1000 and total<=3000:
    print("disscount 500 rs")
elif total>3000 and total <=5000:
    print("disscount 1000 rs")
elif total>5000:
    print("disscount 1200 rs")
else:
    print("no disscount")
"""
"""
#11
a=int(input("enter the number"))
if a%2==0:
    print("even")
elif a%2==1:
    print("odd")
else:
    print("zero")
"""
"""
#12
color=input("enter color")
#color=["red","yellow","green"]
if color=="red":
    print("vehicle stop")
elif color=="yello":
    print("vehicle are ready to go")
elif color=="green":
    print("vehicle can go")
else:
    print("invalid color")
    """
