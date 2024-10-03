"""
#1
a=int(input("enter the number"))
if a>5:
    print(-abs(a))
else:
    print(a)
    """

"""
#2
a=int(input("enter the number"))
if a<10:
    print(a**3)
else:
    print(a)
"""
"""
#3
a=int(input("enter the number"))
if a%2==1:
    print(divmod(a,2))
else:
    print(f"{a} is a even number")
    """
""""
#4
a=eval(input("enter the data"))
if a.isalpha():
    print(a*2)
else:
    print(f"{a} is not alphabate")
  
      """
"""
#5
a=int(input("enter the number"))
if a%6==0:
    print(a**3)
else:
    print(a<<3)
"""
"""
#6
a=int(input("enter the number"))
if a%2==0:
    print(f"{a} is even number")
else:
    print(f"{a} is a odd number")
    """
"""
#7
a=input("enter gender")
age=int(input("enter the age"))
if age>=18:
    print(f"{a} of age {age} eligiable for voting ")
else:
    print(f"{a} of age {age} eligiable  not for voting ")
    """
"""
#8
a=input("enter the chat")
if a.upper():
    print(a.lower())
else:
    print(a)
    """
"""
#9
a=input("enter the chat")
if a.lower():
    print(a.upper())
else:
    print(a)
"""
"""
#10
n1=34
n2=54
if n1>n2:
    print(f"{n1} is greater than {n2}")
else:
     print(f"{n2} is greater than {n1}")
"""
"""
#11
a=int(input("enter the number"))
if a%2==0:
    print(f"{a} is even")
else:
    print(f"{a+1}")
    """
"""
#12
s="python"
if s.title()==True:
    print(s)
else:
    print(s.capitalize())
    """
""""
#13
a=int(input("enter the number"))
if a%2==0:
    print(a/2)
else:
    print(a**3)
"""
"""
#14
a=int(input("enter the number"))
if a%3==0 and a%7==0:
    print(f"{a} is divisable by 3 and 7")
else:
    print(f"{a} is not divisable by 3 and 7")
    """
"""
#15
a=input("enter the string")
if len(a)%2==0:
    print(a[: :-1])
else:
    print(a.upper())
    """
"""
#16
a=int(input("enter the number"))
if a>0:
    print("positive")
else:
    print("negative")
"""
"""
#17
a=eval(input("enter data"))
if isinstance(a,(int,float,bool,complex)):
    print("it is individual data type")
else:
    print("it is collection data type")
    """
"""
#18
s="Python"
c=input("enter character")
if c in s:
    print(f"{c} is present in {s}")
else:
    print(f"{c} is not present in {s}")
    """
"""
#19
D={"a":"apple","b":"ball","c":"cat"}
if len(D)%2==0:
    print(D)
else:
    s=eval(input("enter data"))
    Updated_vale=D.update(s)
    print(D)
"""
