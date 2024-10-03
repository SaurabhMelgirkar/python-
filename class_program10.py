"""
#exception handling
l=[1,4,5,7]
try:
  print(l.index(9)) 
except :
    print("handling error")

try:
   print(l.index(9)) 
except ValueError as msg :
   print("value is not found")
   print(msg)

"""
"""
a=[1,2,3,4]
try:
    a[5]
except IndexError:
    print("error is handling")
except ZeroDivisionError:
    print("handling")
except TypeError:
    print("handling")
finally:
    print("programer is handling error")
try:
    a[5]
except (ZeroDivisionError,IndentationError,ValueError,IndexError):
    print("handling")
"""
"""
a=[1,2,3,4]
try:
    a[2]
    try:
        a[7]
    except:
        print("error")
except:
    print("no error")
    """
"""
a="program"
try:
   print(a[10])
   try:
      print(a[20])
   except:
      print("error")
except:
   print("no error")
   """
"""
a="python"
try:
    a[10]
    try:
        a[20]
    except:
        print("error1")
except:
    print("error 2")
else:
    print("no error")
finally:
    print("wow")
"""
"""

class metroerror (Exception):
    pass

def check(a):
   if a>0:
      print("positive")       
   else:
      raise metroerror
check(7)
check(-7)
      
""" 
#lambda function
"""   
x=lambda a:f"{a}is even number" if a%2==0 else f"{str(a)[::-1]} is odd number"
print(x(35))
"""
"""
#1
x=lambda a:f"{a**2} is squre"f" {a**3} is cube"
print(x(5))
"""
"""
#2
x=lambda a:f"{a} is palendrome"if str(a)==str(a)[::-1] else f"{a} is not palendrome"
print(x(331))
"""
"""
#3
x=lambda a: f"{abs(a)} " if a<0 else f"{a}"
print(x(2))
"""
"""
#4
#a={"hello":"Sony","How":"are","you":"bye"}
x=lambda a:f"{dict.keys(a)}"
print((x({"hello":"Sony","How":"are","you":"bye"})))
"""
#5
"""
x=lambda a:f"{a}is even number" if a%2==0 else f"{str(a)[::-1]} is odd number"
print(x(35))
"""

#6
"""
x=lambda a:f"{a[0]} and {a[-1]}" if isinstance(a,(str,list,tuple)) else f"it is not seqyuence"
print(x("saurabh"))
"""
#7
"""
x=lambda a:f"{len(a)}" if isinstance(a,(str,list,tuple,bool,dict,set)) else f"it is not iterable"
print(x("saurabh"))

"""
#8
"""
l=[2,3,4,5,6]
x=lambda l:[i**2 for i in l]
print(x(l))
"""
#9
"""
l=["nayana","kayak","mom","school","bag","dad"]
x=lambda l:[i==i[::-1] for i in l]
print(x(l))
"""
#10
"""

l=[100,200,300,400,500]
x=lambda l:list(enumerate(l))
print(x(l))
"""
#11
"""
x=lambda l: f"{len(l)}"if isinstance(l,(list,str,tuple)) else f"{type(l)}"
print(x({12:34}))
"""
#12
"""
x=lambda l:f"{l} is divisable by 5 & 3" if l%3==0 and l%5==0 else f"{l} is not divisable by 5 & 3"
print(x(30))
"""
#13
"""
import math as m
x=lambda l: f"squre of {l} is {l**2}" if l%2==0 else f"squre root  of {l} is {m.sqrt(l)}"
print(x(3))

"""
#14
"""
x=lambda l:f"string {l} len {len(l)} is even "if len(l)%2==0 else f"string {l[::-1]} len {len(l)} is odd "
print(x("helllo"))
"""
#15
"""
result = lambda s: ((s, len(s)), {'value': s, 'length': len(s)})
print(result("saurasbh"))
"""