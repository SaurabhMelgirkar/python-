"""
#1
n=int(input("enter the number"))
for i in range(2,n):
    if n%i==0 :
        print(f"{n} is  not prime prime")
        break
    else:
        print(f"{n} is  prime number")
        break

"""
"""
#2
n=int(input("enter the number"))
x=str(n)
res=0
for i in x:
    res=res + int(i)**3
if res==n:
    print("  armstrong")
    
else:
     print(" not armstrong") 
"""
"""
#3
s = 'life is full of surprises and miracles'
length=" "
for i in s.split():
    if len(length)<len(i):
        length=i 
print(length)  
"""
#4