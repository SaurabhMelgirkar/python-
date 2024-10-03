#ILLED kewyord
#1
"""
y=['walmart',"fb","sql","python","facebook"]
def check(y):
    l=[]
    for i in y:
     if len(i)%2==0:
        l.append(i[::-1])
    yield l
s=check(y)
print(next(s))
"""
"""
#2
def check(a,b):
    sum1=a+b
    sub=a-b
    mul=a*b
    div=a/b
    #if sum1 and sub and mul and div%5==0:
    yield sum1
    yield sub
    yield mul
    yield div
s=check(10,5)
print(next(s))
print(next(s))
print(next(s))
print(next(s))
"""
#2
"""
l=[34,55,60,56,78,90,25,40]
def check():
    l2=[]
    for i in l:
        if i%5==0:
            l2.append(i)
            yield l2
s=check()
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
#print(next(s))

"""
"""
#3
import math as m
l=[25,36,49,81,9,16]
def check():
    
    for i in l:
        a=m.sqrt(i)
        yield a
s=check()
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
#print(next(s))
#print(next(s))
"""
"""
l=["instagram","facebook","whatsapp","meta","oracle"]
def fun():
    d={}
    for i in l:
        d[i]=len(i)
        #x=len(i)
        yield tuple ((d,))
    
s=fun()
print(next(s))
            
"""
"""
l=["flipkart","Amazon",78,[2,3,4],78,9.87,(5,3),45.36]
def check():
    for i in l:
        if isinstance(i,(float,int)):
            yield i
            
s=check()
print(next(s))
"""
"""

l=["flipkart","Amazon",78,[2,3,4],78,9.87,(5,3),45.36]
def check():
    for i in l:
        if isinstance(i,(int,float,bool,complex)):
            i=str(i)
            r=(i[::-1])
            yield r
            
            
s=check()
print(next(s))
"""
"""

l=["alexa","siri","google","cortrena"]
def check():
    for i in l:
        if len(i)%2==1:
            yield i
s=check()
print(next(s))
print(next(s))
"""
"""
l=[2,3,4,5,6,7]
def check():
    o=[]
    e=[]
    for i in l:
     if i%2==0:
         a=i**2
         e.append(a)
         yield e
     else:
         b=i**3
         o.append(b)
         yield o
s=check()
print(next(s))
print(next(s))
"""
"""
#wap to return a list if words is of even length reverse it


l=["hello","world","python","apple","google","walmart"]
def check():
    for i in l:
        if len(i)%2==0:
            a=i[::-1]
            yield a
        else:
            yield i
s=check()
print(next(s))
print(next(s))
"""

#wap to generate a list if it is individual data type

#reverse it else keep it as it is

"""
a=["good",45,[1,2],78.6,(4,5),8+7j,{9,7},False,{"a":75}]    
def check():
    for i in a:
        if isinstance(i,(int,float,bool,complex)):
            i=str(i)
            r=(i[::-1])
            yield r
        else:
            yield i
s=check()
print(next(s))
print(next(s))
print(next(s))

"""
"""
s="python is a programming language and programming is part of life"

def reverse(s):
    d={}
    for i in s.split():
        if i[0] not in d:
        
            d[i[0]]=[i]
        else:
            d[i[0]]+=[i]

    yield d

print(list(reverse(s)))    
"""
"""
# file handling
import os 
print(os.getcwd())
print(os.chdir(r"D:\box"))
print(os.getcwd())
#os.mkdir("ball")
#os.mkdir("bat")
#os.rmdir("ball")
print(os.listdir())
#os.rename("bat","code")
#f=open("saurabh.txt","x")
#f2=open("melgirkar.txt","x")
#os.popen("saurabh")
#os.remove("saurabh.txt")
#print(os.path.getsize("melgirkar.txt"))


"""
#isslice
"""   
import os 
print(os.getcwd())
print(os.chdir(r"D:\box"))
print(os.getcwd())
with open("melgirkar.txt","r")as file:
#    print(file.writelines("day one class \n"))
  #  print(file.writelines("hello \n"))
   # print(file.writelines("sunday \n"))
    #print(file.writelines("monday \n"))
   # os.popen("melgirkar.txt")
#    print(file.tell())
   # print(file.seek(2))
    #print(file.read())
    from itertools import islice
    with open("melgirkar.txt","r")as file:
"""
"""
import os 
print(os.getcwd())
print(os.chdir(r"D:\box"))
print(os.getcwd())

import csv
with open("laptop.csv","w",newline='')as file:
    data=csv.writer(file)
    data.writerows([["apple",100,500],["graphes",500,1000],["banana",20,400]])
   # data.writerow(["saurabh","raju","vicky",'rohan'])
    #data.writerow([100,200,300,400])
    os.popen("laptop.csv")


"""
"""
import os 
print(os.getcwd())
print(os.chdir(r"D:\box"))
print(os.getcwd())
import csv
with open("laptop.csv","r",newline='')as file:
    #data=csv.DictWriter(file,["sname","branch"])
    #data.writeheader()
    #data.writerows([{"sname":"saurabh","branch":"cs"},{"sname":"raju","branch":"it"}])
    #data.writerow({"sname":"saurabh","branch":"it"})
    #os.popen("laptop.csv")
    #x=csv.reader(file)
    #print(list(x))
    #for i in x:
     #   print(i)
    x=csv.DictReader(file)
    print(list(x))
    


"""
#piklung 
""""
import os
import pickle
with open("saurabh.pkl","wb")as file:
    data=pickle.dump(["a","b","c"],file)
    #x=pickle.load(data)
    #os.popen("saurabh.pkl")
with open("saurabh.pkl","rb")as file:
    data=pickle.load(file)
    os.popen("saurabh.pkl")
    #print(data)
""""
""""

import pickle
s="python"
x=pickle.dumps(s)
print(x)
y=pickle.loads(x)
print(y)
"""
#exception handling

    
    
    




