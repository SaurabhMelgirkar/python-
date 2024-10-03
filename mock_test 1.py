#1.WAP to replace one string with another string
"""
#with using replace
s = 'hello world' #exp o/p : 'hello Universe
print(s.replace("hello world","hello universe"))

#without using replasce

s = 'hello world'
target = 'world'
replacement = 'Universe'

result = ''
i = 0

while i < len(s):
    if s[i:i+len(target)] == target:
        result += replacement
        i += len(target)
    else:
        result += s[i]
        i += 1
print(result)

"""

#2.WAP to reverse each element in a list,then reverse entire list
"""
names = ['apple', 'google', 'yahoo', 'walmart']
print(names[::-1])
"""
#3.WAp to sort the list which is mix of both even & odd,
#  the sorted list should have odd numbers first & then even numbersin sorted order
"""
l=[3,4,1, 7,2,12,8,9,11,16,13]
even=[]
odd=[]
for i in l:
    if i%2==0:
     even.append(i)
     even.sort()
    else:
       odd.append(i)
       odd.sort()
print(even)
print(odd)
"""

#9.WAP to separate vowels & consonants from a
#  string. s = 'hello guys good morning welcome to programming class'
#  #exp o/p :{'vowels': [e,o,u,o,o..], 'conso':[h,l,l]}
"""
s = 'hello guys good morning welcome to programming class'
vovels=[]
constraints=[]
for i in s:
    if i in "aeiouAeiou":
        vovels.append(i)
    else:
        constraints.append(i)
print(vovels)
print(constraints)
"""        
# 5.WAp to remove duplicates from the list without usingempty list or set
"""
l = [1, 2, 3, 4, 1, 2, 3, 4, 4, 5]

i = 0
while i < len(l):
    j = i + 1
    while j < len(l):
        if l[j] == l[i]:
            l.pop(j)
        else:
            j += 1
    i += 1

print(l)
"""

# 4.WAP to print maximum sum of 3 numbers & minimum sum of 3numbers
"""
numbers = [18,15,20,25, 30,35, 40, 5,10,15]
numbers.sort()
print(numbers)
min=numbers[0]+numbers[1]+numbers[2]
print(min)
max=numbers[-1]+numbers[-2]+numbers[-3]
print(max)
"""
#7..WAP to get given o/p:
"""
l = ['sun flower', 'lilly flower', 'Marigold flower', 'lion animal',
'tiger animal', 'eagle bird', 'snake animal', 'lotus flower', 'pigeon bird']
d={}
for i in l:
     x=i.split()
     if x[1] not in d:
            d[x[1]]=[x[0]]
     else:
            d[x[1]]+=[x[0]]
print(d)
    #print(i[0])

    #print(type(i))
    #for j in l:
"""

# 8.WAP to take 2 list remove repeated elements in both & return
#a list of unique elements without typecasting to set
"""
l1 = [2, 3, 5, 7, 5, 2]
l2 = [5, 4, 2, 7, 8, 4, 5]
l3=l1+l2
l4=[]
for i in l3:
    if i not in l4:
        l4.append(i)
print(l4)
"""
# 6.Real time scenario based OOPs
#Requirements: ============
#Login into Qspiders class
#username : It should be mail address or phone number
#mail id : It should have 1 @ max of 2 '.' and should ends
#with .com
#phone number : the length should be 13 including '+' pwd: The length should be 8 characters
#atleast 1uc, 1lc, 1spl, 1digit
"""

from abc import ABC, abstractmethod
import re

class User(ABC):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @abstractmethod
    def is_valid(self):
        pass

class EmailUser(User):
    def is_valid(self):
        email_regex = r'^[\w.-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}$'
        return re.match(email_regex, self.username) is not None

class PhoneUser(User):
    def is_valid(self):
        phone_regex = r'^\+\d{12}$'
        return re.match(phone_regex, self.username) is not None

class PasswordValidator:
    def __init__(self, password):
        self.password = password

    def is_valid(self):
        password = self.password

        if len(password) < 8:
            return False

        if not re.findall(r"[a-z]", password):
            return False

        if not re.findall(r"[A-Z]", password):
            return False

        if not re.findall(r"\d", password):
            return False

        if not re.findall(r"[@$!%*#?&]", password):
            return False

        return True

class Login:
    def __init__(self, username, password):
        if '@' in username:
            self.user = EmailUser(username, password)
        else:
            self.user = PhoneUser(username, password)
        self.password_validator = PasswordValidator(password)

    def login(self):
        if self.user.is_valid() and self.password_validator.is_valid():
            print("Login successful")
        else:
            print("Invalid credentials")

username = "abc@example.com"
password = "Password123!"
login = Login(username, password)
login.login()
"""    
# 10.WAP to suggest a Student to take which course in QSP/JSP/PYSP
# lst = ['QSP', 'JSP', 'PYSP']
# names = ['Testing', 'Development']
"""
lst = ['QSP', 'JSP', 'PYSP']
names = ['Testing', 'Development']

choice = input("choose between 'QSP', 'JSP' and 'PYSP' : ")

if choice in lst:
    print(f'You can take subjects like: {names}')
else:
    print('Enter valid name')
"""

