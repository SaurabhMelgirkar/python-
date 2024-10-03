"""
t=(1,10+2j,"hello",True)
for i in t:
    print(i,end=" ")
"""
"""
t=[1,10+2j,"hello",True]
for i in t:
    print(i,end=" ")
"""
"""
t={1,10+2j,"hello",True}
for i in t:
    print(i,end=" ")
"""
"""
t="hi i am saurabh "
for i in t:
    print(i,end="")
    """
"""
d={10+2j:20,"hello":True,False:12+9j,1:2}
for i in d:
    print(i,end=" ")
"""
"""for i in range(120,142):
    print(i,end=" ")
"""
"""
l1=[]
l2=[]
for i in range(1,21):
    if i%2==0:
        l1.append(i)
        
    else:
        l2.append(i)
print(l1)
print(l2)
"""
""""
#2
s="hello123"
l1=[]
l2=[]
l3=[]
for i in s:
    if i in"aeiou":
        l1.append(i)
    elif i.isdigit():
        l2.append(i)
    else:
        l3.append(i)
print(l1)
print(l2)
print(l3)

"""
"""
#3
l=["rahul","kapil","patil"]
for i  in l:
    print(i.capitalize() end=" ")
"""
"""
#4
l=["hello",1,23.4,5+6j,"guys",True,False]
for i in l:
    if isinstance(i,(int,float,bool,complex)):
        print(i,end=" ")
        """
"""
#5
l=["hello",1,23.4,5+6j,"guys",True,False]
sum=0
for i in l:
    if isinstance(i,(int,float,bool,complex)):
        sum=sum+i
print(sum)
"""
"""
a="saurabh"
print(list(enumerate(a)))
for i in enumerate(a):
    print(i)
    """
"""
a="saurabh"
x=list(reversed(a))
print(list(enumerate(x)))
"""
"""
#6
s="India got the independence in the year 1974"
alpha=0
digit=0
space=0
for i in s:
    if i.isalpha():
        alpha=alpha+1
    elif i.isdigit():
        digit=digit+1
    else:
        space=space+1
print(alpha)
print(space)
print(digit)

        """
"""
#7
e="hello world"
d={}
for i in e:
    d[i]=ord(i)
print(d)
"""
"""
#8
s="hello world sentence i am saurabh"
count_space=0
count_words=0
for i in s:
    count_words=(len(str.split(s)))
print(f"no of wotrds are {count_words}")


"""
"""
#9
names=["apple","google","yahoo","microsoft","gmail","walmart","brave"]
d={}
for i in names:
    if len(names)%2==0:
        d[i]=(i)
    else:
        d[i]=i[: :-1]
                      
print(d)
#output:-->{'apple': 'elppa', 'google': 'google', 'yahoo': 'oohay', 'microsoft': 'tfosorcim', 'gmail': 'liamg', 'walmart': 'tramlaw'}
"""
"""
#10
num=int(input("enter the number"))
factorial = 1

if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial *= i
        print(f"The factorial of {i} is {factorial}")
"""




   


    
"""
#11
l=["yellow","red","black","pink","orange","green","red","pink","yellow"]
d={}
count=0
for i in l:
    d[i]=l.count(i)
print(d)
"""
"""
#12
s="Never Give Up"
count=0
for i in s:
    count+=1
print(count)
"""
"""
#13
x="you did it guys"
for i in x:
    rev=x[ : :-1]
    
print(rev,end="")
"""
"""
#14
s="hello python"
for i in s:
    alternative_char=s[0: :2]
print(alternative_char,end=" ")
"""
"""
x="you did it guys"
res=" "
for i in x:
    res=i+res
print(res)
"""
"""
#15
s="tomorrow is weekend and non-veg special"
d={}
for i in s.split():
    e=s.split()
    d[i]=e.index(i)

print(d)
"""
"""
#16
s="tomorrow is weekend and non-veg special"
d={}
for i in s.split():
    e=s.split()
    d[i]=len(i)
print(d)
"""
"""
#17
s="sunday"
d={}
for i in s:
    d[i]=i.upper()
print(d)
"""
"""
#18
l=[89,51,111,77,108,120]
d={}
for i in l:
    d[i]=chr(i)
print(d)  
"""
"""
#19
s="sunday"
d={}
for i in s:
    d[i]=ord(i)

print(d)
"""
"""
#20

lst= ['hai', 'hello', 'python', 'world', 'jingalala']
for i in range(len(lst)):
    del lst[0]
print(lst)    
"""
"""
#21
s="Today is Tuesday and attending python session "
d={}

for i in s.split():
    e=s.split()
    if i.endswith(("a","e","i","o","u")):
        d[i]=len(i)
print(d)
"""
"""
#22

s="hi hello good morning welcome to python session"
d={}
count=0
for i in s.split():
    if i[0] not in d:
        d[i[0]]=[i]
    else:
        d[i[0]]=[i]
print(d)
"""
"""
#23 - no
s="hello python"
d={}
count=0

for i in s:
    d[i]=(i)
print(d)
    

"""
"""
#24
s="tomorrow is weekend and non-veg special"
d={}
for i in s.split():
      
      d[i]=i[ : :-1]
print(d)

    
"""
"""
#25
l = [1, 2, 3, 4]
l=str(l)
res=" "
for i in l:
    res=i+res
print(res)
"""

#assignment question
"""
#1
s = 'Sony12India567pvt21ltd'
count=0
for i in s:
    if i.isdigit():
        count=count +int(i)
        
print(count)
"""
"""
#2

l = [1, 2, 3, 4, 6, 7, 10]
for i in range(1,10):
    if i not in l:
        l.insert(i-1,i)
print(l)
"""
"""
#3 
d=[1,2,3,4,5,6,7,1,2,3,4] 
new_list = []

for i in d:
  if i not in new_list:
    new_list.append(i)

print(new_list)
"""

"""

#5 --no
l = ['apple', 123, 'google', '45.6', 'yahoo', [1,2,3],True, (1,3,7), 6+3j]
for i in l:
 if isinstance(i,int):
            print(i)
    
"""

"""
#4
s = "hellohai"
a = []
new_str = ""

for i in s:
  if i not in a:
    a.append(i)
    new_str += i
  else:
    new_str += "-"
print(new_str)

""
#23 copy
s = "hello python"
char_dict = {}
for i, char in enumerate(s):
  if char in char_dict:
    char_dict[char].append(i)
  else:
    char_dict[char] = [i]
print(char_dict)
"""
