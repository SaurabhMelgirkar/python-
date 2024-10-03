"""
a=int(input("enter"))
b=int(input("enter"))
c=int(input("enter"))
print(f"{a},{b},{c}")
a=a*b*c
b=a//b//c
c=a//b//c
a=a//b//c
print(f"{a},{b},{c}")
"""
"""
#2
a=int(input("enter"))
b=int(input("enter"))
c=int(input("enter"))
print(f"{a},{b},{c}")
a=a^b^c
b=a^b^c
c=a^b^c
a=a^b^c
print(f"{a},{b},{c}")
"""
"""
#3
a=int(input("enter"))
b=int(input("enter"))
c=int(input("enter"))
print(f"{a},{b},{c}")
a=a+b+c
b=a-b-c
c=a-b-c
a=a-b-c
print(f"{a},{b},{c}")
"""
"""
#4
a=int(input("enter"))
b=int(input("enter"))
c=int(input("enter"))
print(f"{a},{b},{c}")
d=a
a=b
b=c
c=d
print(f"{a},{b},{c}")
"""
"""
#5
a=int(input("enter"))
b=int(input("enter"))
c=int(input("enter"))
print(f"{a},{b},{c}")
a,b,c=c,b,a
print(f"{a},{b},{c}")
"""
# if and else program
"""
#1
n=int(input("enter number"))
if n%2==0:
    print(f"{n} is even number")
else:
    print(f"{n} is odd number")
"""
"""
#2
n=int(input("enter number")) 
if n//2*2==n: #n//2*2==n
    print(f"{n} is even number")
else:
    print(f"{n} is odd number")
    
"""
"""
#3
n=int(input("enter number"))
if n&1==0:#n&1==1
    print(f"{n} is even number")
else:
    print(f"{n} is odd number")
"""
"""
#4
n=int(input("enter number"))
if n|1==n+1:#n|==n
    print(f"{n} is even number")
else:
    print(f"{n} is odd number")
"""
"""
for i in range(1,3):
    for j in range (1,4):
        print(j,end=" ")
"""
# pattern program
"""
#1
row=int(input("enter no of rows "))
col=int(input("enter the column"))
for i in range(row):
    for j in range(col):
      print("*",end=" ")
    print()
"""
"""
#2
row=int(input("enter no of rows "))
col=int(input("enter the column"))
val=1
for i in range(row):
    for j in range(col):
      print(val,end=" ")
    print()
    val=val+1
"""
"""
#3
row=int(input("enter no of rows "))
col=int(input("enter the column"))
val=1
for i in range(row):
    for j in range(col):
      print(val,end=" ")
    print()
    val=val+1
    if val>9:
       val=1
"""
"""
#4
row=int(input("enter no of rows "))
col=int(input("enter the column"))
val=1
for i in range(row):
    for j in range(col):
      print(val,end=" ")  
      val=val+1
      if val>9:
            val=1
    print()
"""
"""
row=int(input("rows"))
col=int(input("column"))
val=row
for i in range(row):
    for j in range(col):
        print(val, end=" ")
    print()    
    val=val-1
    if val>=10:
        val=9
"""      
"""
row=int(input("rows"))
col=int(input("column"))

for i in range(row):
    val=col
    for j in range(col):
        print(val, end=" ")
        val=val-1
    print()    
"""
"""

row=int(input("rows"))
col=int(input("column"))
val=ord("A")
for i in range(row):
    for j in range(col):
        print(chr(val), end=" ")
    print()    
    val=val+1
    if val >ord("Z"):
     val=ord("A")
    
"""
"""

row=int(input("rows"))
col=int(input("column"))
val=ord("a")
for i in range(row):
    for j in range(col):
        print(chr(val), end=" ")
    print()    
    val=val+1
    if val >ord("z"):
     val=ord("a")
"""
"""
row=int(input("rows"))
col=int(input("column"))
for i in range(row):
    val=ord("a")
    for j in range(col):
        print(chr(val), end=" ")
        val=val+1
    print()       
    if val >ord("z"):
     val=ord("a")
"""
"""""
n=int(input("enter"))
for i in range(n):
    for j in range(n):
        if i>=j:
            print("*" ,end= " ")
        else:
            print( " ",end=" ")
    print( )
    
"""
"""
n=int(input("enter"))
val=1
for i in range(n):
    for j in range(n):
        if i>=j:
            print(val ,end= " ")
        else:
            print( " ",end=" ")
    print( )
    val=val+1
    if val>9:
        val=1
        """
"""
n=int(input("enter"))
for i in range(n):
    val=1
    for j in range(n):
        if i>=j:
            print(val ,end= " ")
            val=val+1
            if val>9:
             val=1
        else:
            print( " ",end=" ")
            
    print( )
"""
"""
n=int(input("enter"))
val=n
for i in range(n):
    for j in range(n):
        if i>=j:
            print(val ,end= " ")
        else:
            print( " ",end=" ")
    print( )
    val=val-1
"""
"""
n=int(input("enter"))

for i in range(n):
    val=n
    for j in range(n):
        if i>=j:
            print(val ,end= " ")
            val=val-1
        else:
            print( " ",end=" ")
    print( )
"""  
"""  
n=int(input("enter"))
val=ord("A")
for i in range(n):
    
    for j in range(n):
        if i>=j:
            print(chr(val) ,end= " ")
            
        else:
            print( " ",end=" ")
    print( )
    val=val+1

"""
"""
# i stands for row & j stands for column
n=int(input("enter"))
for i in range(n):
    val=ord("A")  
    for j in range(n):
        if i>=j:
            print(chr(val) ,end= " ")
            val=val+1          
        else:
            print( " ",end=" ")
    print( )
"""
"""
n=int(input("enter"))
val=ord("A")+n-1
for i in range(n):
    
    for j in range(n):
        if i>=j:
            print(chr(val) ,end= " ")
            
        else:
            print( " ",end=" ")
    print( )
    val=val-1
"""
"""
n=int(input("enter"))
for i in range(n):
    val=ord("A")+n-1
    for j in range(n):
        if i>=j:
            print(chr(val) ,end= " ")
            val=val-1          
        else:
            print( " ",end=" ")
    print( )
"""
"""

n=int(input("enter"))
for i in range(n):
    for j in range(n):
        if i<=j:
            print("*" ,end= " ")
        else:
            print( " ",end=" ")
    print( )
    """
"""
#diamond
n=int(input("enter"))
start=1
space=n-1
for i in range(n):
    for j in range (space):
        print(" ",end=" ")
    for k in range(start):
        print("*",end=" ")
    print()
    start+=2
    space-=1
"""
"""
n=int(input("enter"))
str=1
space=n-1
for i in range(n):
    print(" "*space+"*"*str)
    str+=2
    space-=1
"""
"""
n=int(input("enter"))
for i in range(n):
    for j in range (n-i-1):
        print(" ",end=" ")
    for k in range(2*i+1):
        print("*",end=" ")
    print()
"""
"""
n=int(input("enter"))
for i in range(n):
    print(" "*(n-i-1)+"*"*(2*i+1))
"""
"""
n=int(input("enter"))
val=1
for i in range(n):
    print(" "*(n-i-1)+(str(val)+" ")*(2*i+1))
    val=val+1
    if val>9:
        val=1
"""
"""
n=int(input("enter"))
val=ord("A")
for i in range(n):
    print(" "*(n-i-1)+(str(chr(val))+" ")*(2*i+1))
    val=val+1
"""
"""
n=int(input("enter"))
start=n-1
space=0
for i in range(n):
    for j in range (space):
        print(" ",end=" ")
    for k in range(start):
        print("*",end=" ")
    print()
    start+=2
    space-=1
"""
"""
n=int(input("enter number"))
res=0
while n>0:
 rem=n%10
 res=res*10 +rem
 n//=10
 print(res)
""" 
""""
n=int(input("enter number"))
res=0
zc,oc,ec=0,0,0
while n>0:
 rem=n%10
 if n==0:
  zc+=1
 elif n%2==0:
  ec+=1
 else:
  oc+=1
 n//=10
print(f" zero:{zc},odd:{oc},even:{ec}")
"""
"""
#n=int(input("enter"))
n=1234078
sumodd=0
sumeven=0
for i in str(n):
    if int(i)%2==0:
        sumeven=sumeven + int(i)
    else:
         sumodd=sumodd + int(i)
print(f"sum even{sumeven}, odd sum {sumodd}")
"""
m=int(input("enter"))
n=0
for i in str(n):
    if int(i)>m%10:
        m=i
print(f"max{m}")
        






