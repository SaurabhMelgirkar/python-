"""
#1
a=["Sunil","anil","Suresh","Mahesh","Dinesh"]
for i in a:
    print(i[0],i[-1])
"""
"""
#2

b=[2,4,5,6,7,1]
c=[]
for i in b:
    sq=i**2
    c.append(sq)
print(c)
"""
"""
#3
c=[2,4,5,3,7,9]
d=[]
e=[]
for i in c:
    if i%2==0:
        sq=i**2
        d.append(sq)
    else:
        cub=i**3
        e.append(cub)
print(d)
print(e)
"""
"""
#4
d=[2,4,5,1,8,9,10]
e=[]
for i in d:
    sq=i**2
    cub=i**3
    e.append((sq,cub))
print(e)


"""

"""
#5

names=["prince","Rekha","Madhu","Sindhu","denga","manga"]
rev=[]
for i in names:
     rev.append((i[ : :-1]))
print(rev)
"""
"""
#6
data=[20.12,True,[10,20],"super",{1,2},{"a":10},100,(8,9)]
i_d=[]
c=[]
for i in data:
    if isinstance(i,(int,complex,float,bool)):
        i_d.append(i)
    else:
        c.append(i)
print(i_d)
print(c)
"""
"""
#7
books={"love story":["Harish",30],"biography":["padam",150],"animals":["vimala",75]}
for i in books.values():
         print(i[0])
"""
"""
#8
char=["a","M","i","A","M","I","i","H","a","H"]
d={}
for i in char:
    d[i]=char.count(i)
print(d)
"""
"""
#9
d={"apple":45,"mango":67,"cherry":90,"berry":23}
p={"Kashmir":"India","America":"us","UK":"Toronto","Africa":"Uganda"}

for i in zip(d,p):
    print(i)
"""
"""
#10
d={"apple":45,"mango":67,"cherry":90,"berry":23}
p={"Kashmir":"India","America":"us","UK":"Toronto","Africa":"Uganda"}
for i in zip(d,p):
    if len(i[0])%2==0:
        print(i)
    
"""
"""
#11
l1=[10,20,30,40]

l2=[78,44,11,99]

l3=[1,2,3,4]
for i in zip(l1,l2,l3):
    print(sum(i))
"""
"""
#12
d={"apple":45,"mango":67,"cherry":90,"berry":23}

p={"Kashmir":"india","America":"us","UK":"Toronto","Africa":"Uganda"}
for i in zip(d.values(),p.values()):
    print(i)
"""
"""
#14

l = ['sun flower', 'Lilly flower', 'Marigold flower', 'lion animal', 'tiger animal', 'eagle bird', 'snake animal', 'lotus flower', 'pigeon bird']
d = {}
for item in l:
  key = item.split()[0]
  value = item.split()[1]
  if key in d:
    d[key].append(value)
  else:
    d[key] = [value]

print(d)
"""
#13

    
"""
l=[1,2,7,9,4,3,10,11,8,2,3]
for i in l:
    if i>=10:
        break
    print(i,end=" ")
    """
"""
s="hello guys you are working really hard super"
for i in s:
    if i=="y":
        continue
    print(i,end=" ")
    """
"""
for i in range(1,11):
    if i==5:
        continue
    print(i,end=" ")
    """
"""
l=[1,5,-2,-45,55,88,-100,-63]
for i in l:
      if i<0:
        break
      print(i,end=" ")
      """
"""
#wap to skip all the vowels in the given string

s="good morning guys welcome to python session"
for i in s:
    if i in "aeiou":
        continue
    print(i,end=" ")
    """
"""
#13

#13.WAP to print sum of internal and external list

l = [[1,2,3], [4,5,6], [7,8,9]]
a=[]
b=[]
c=[]
for i in l:
    if  l[0]:
        a.append(i[0])
        if l[1]:
            b.append(i[1])
        if l[2]:
            c.append(i[2])
        


sum1=a[0]+a[1]+a[2]
sum2=b[0]+b[1]+b[2]
sum3=c[0]+c[1]+c[2]
print(sum1)
print(sum2)
print(sum3)
print(sum1 + sum2 + sum3)

"""
"""
#14
 
l = ['sun flower', 'Lilly flower', 'Marigold flower', 'lion animal', 'tiger animal', 'eagle bird', 'snake animal', 'lotus flower', 'pigeon bird']
d={}
for i in l:
    x=i.split()
    if x[1] not in d:
        d[x[1]]=[x[0]]
    else:
        d[x[1]]+=[x[0]]
print(d)

"""
"""
#14

l = [[1,2,3], [4,5,6], [7,8,9]]
res=[]
d=[]
for i in l:
    sum0_internal=0
    external=0
    for j in i:
        sum0_internal+=j
    res.append(sum0_internal)
    for k in i:
        external+=k
        d.append(external)
print(d)
print(res)


"""
"""
s=[1,-2,3,-1,7,-11,12]
for i in s:
    if i>0:
        continue
    print(i)

"""
"""
x="your day will osm"
for i in x:
    if i=="a":
        break
    print(i) 
"""
"""
s="programming part in class"
for i in s:
    if i in s=="aeiou":
        continue
    print(i,end=" ")   
    
        
"""
"""
a="saurabh"
for i in a:
    r=list(reversed(a))
print(r, end=" ")
"""
"""
a="saurabh"
for i in a:
    r=list(enumerate(a))
print(r)      
"""
"""
a="one two  three four five"
b=""
i=0
while i<len(a):
    if i%2==0:
     b=str(reversed(a[i]))
     print(b)
    i=i+1
    """
"""
l=[1,2,3,4,5,6,7,8,9]
e=[]
o=[]
i=1
while i<len(l):
    if l[i]%2==0:
        e.append(i)
        i=i+1
    else:
        o.append(i)
        i=i+1
print(e)
print(o)
"""
"""
s1="good"
s2="well"
i=0
while i<len(s1) :
  a=list(zip(s1,s2))
  i=i+1
print(str(a))
"""
s="012345678912"
i=0
l=[]

while i<=len(s)-1:
    a=s[i].split(s)
    print(a)
    
    i=i+1
    