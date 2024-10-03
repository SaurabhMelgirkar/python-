#1.wap to check whether the given number is odd, if odd store the given number in tuple(take user input)
"""
original_tuple = (1, 2, 3)
num=eval(input("enter number"))

if num%2==1: 
    appended_tuple = original_tuple + (num,)
    print(appended_tuple)

else:
    print(f"{num} is not odd number")

"""
#2 wap to check whether a given values last digit is greater than 5 or not, if greater, perform the bitwise right shift operator(skipping value 2) (take user input)

"""

no=int(input("enter the number"))
if no%10>5:
    bin(no)
    a=no>>2
    print(a)
    #print("it is greater than 5")
else:
    print(f"{no%10} is not greater than 5")
    
"""

#3.wap to check whether a given number is a integer and odd number. If condition 
# is satisfied, the integer is divisible by 5 and display the result (take user input)
"""
no=eval(input("enter the number"))
if isinstance(no,int) and no%2==1:
    if no%5==0:
        print(f"{no} is integer and odd number as well as it is divisable by 5")
    else:
        print(f"{no} is integer and odd number but it is not  divisable by 5")
else:
    print(f"{no} is not integer or odd number")
"""

#4.wap to check whether the given value is an integer or not, if integer 
# the given value is converted into string and display the result (take user input)
"""
no=eval(input("enter the data"))
if isinstance(no,int) :
    convet=str(no)
    print(convet)
    print(type(convet))
else:
    print(f"{no} is not integer")
"""
# 5.wap to check whether the given two integer are equal or not,
#  if both are equal, perform addition and display the result (take user input)
"""
no1=int(input("enter no1"))
no2=int(input("enter no2"))
if no1==no2:
    add=no1+no2
    print(f"{no1} and {no2} are equal and addition of this two number is {add}")
else:
    print(f"{no1} and {no2} are  not equal ")

"""
#6.wap to check whether a character is in the lowercase or not,
#  if the lower case, perform the replication operation on that
#  characters(take user input)
"""
char=input("enter any character")
if char.islower():
    a=char*2
    print(a)
else:
    print(f"{char } is not in lower case")
"""
#7.wap to check whether a given character is vowel or not if it is vowel
#  print next character else print previous character(take user input)
"""
char=input("enter the char")
if char in ("aeiouAEIOU"):
    a=ord(char)+1
    print(chr(a))
else:
    b=ord(char)-1
    print(chr(b))

"""
#8.wap to check the given number is even then convert 
# negative else print as it is (take user input)
"""
no=int(input("enter the number"))
if no%2==0:
    print(-abs(no))
else:
    print(no)

"""
#9.wap to Turn FAN ON or OFF (condition  1-->FAN ON   0-->FAN OFF)
"""
no=int(input("enter 0 or 1"))
if no==0:
    print("fan off")
elif no==1:
    print("fan on")
else:
    print("invalid input")
"""
#10.write a program to accept percentage from the
#  user and display the grade according  to the following criteria
"""
per=eval(input("enter the percentage"))
if per>90:
    print("grade A")
elif per >80 and per <=90:
    print("grade B")
elif per >=60 and per<=80:
    print("grade C")
else:
    print("grade D")  
"""
#11.Accept Three sides of triangle and check whether the triangle is possible
#  or not (take user input) 
# (triangle is possible only when sum of any two sides is greater than 3rd side)
"""
side1=int(input("enter side 1"))
side2=int(input("enter side 2"))
side3=int(input("enter side 3"))
if side1+side2>side3 or side1+side3>side2 or side3+side2>side1 :
    print("it is traingle")
else:
    print("it is not traingle")
"""
#12.wap to check the given number is digit or not try it both with 
# and without using inbuilt function (take user input)
"""
no=eval (input("enter the digit"))
if isinstance(no,int) and no>=0 :
    print("it is digit")
else:
    print("it is not digit")
"""
#13.WAP to check the first digit of given number is even or odd
"""
num=578
a=num//100
if a%2==0:
    print(f"first digit of number {num} is {a} and it is even ")
else:
    print(f"first digit of number {num} is {a} and it is odd ")
"""
#14.WAP to check whether the given number lies between 1 to 19,
#  if it is true square that number or else false cube that number
#   and display the number.

"""
no=int(input("enter the number"))
if no in range(1,20):
    print(f"squre of {no} is {no**2}")
else:
    print(f"cube of {no } is {no**3}")
"""
# 15.WAP to check whether the student has passed or failed. If the student 
# got more than 40 marks, print
#  ‘PASS’ along with those marks, if it is not printed ‘
# FAIL’ along  with those marks.
"""
marks=int(input("enter your marks"))
if marks>40:
    print(f"your marks is {marks } you are pass")
else:
    print(f"your marks is {marks } you are fail")
"""

#16.WAP to check whether a given string of first character is alphabet or not if
#  the alphabet prints, reverse the string or else print the middle character.
"""
value=input("enter the string")
if value[0].isalpha():
    print(value[::-1])
else:
    a=len(value)//2
    print(value[a])
"""
#17.WAP to check whether a given string is less than 3 characters, 
# to print the entire string otherwise 
# to print after third positions to the remaining string.
"""
value=input("enter the string")
if len(value)==3:
    print(value)
else:
    print(value[3::1])    
"""
#18.Ravi would like to buy a red pen. The cost of the pen should be 10RS.
#  If the pen is available in the shop, he will buy the pen.
# If it is not there he will come out of the shop.
"""
shop={"pencil":5,'rubber':2,'red pen':10,'blue pen':20}
if "red pen" in shop.keys():
    print(f"it is avaliable  ")
else:
    print("it is not avaliable")
"""
#19.WAP to check length of both string collections are equal or not.
#  if both are equal print the concatenation the two strings and display,
#  or else if any one of the collection not equal print both the collections 
# with lengths  

# oroperty decoreator
"""
class Demo:
    def __init__(self,product):
        self.produt=product
    @property
    def getter_(self):
        print("getting value")
        return self.produt
    @getter_.setter
    def setter_(self,product):
        print("setting the product")
        self.produt=product
    @getter_.deleter
    def deleter(self):
        del self.produt
t=Demo("watch")
print(t.getter_)
t.setter_=("phone")
print(t.getter_)
del t.getter_
print(t.getter_)
"""        

#monkey patching
"""
class Test:
    def __init__(self,x):
        self.x=x
    def get_data(self):
        print("taking the data from source code")
    def f1(self):
        self.get_data()
    def f2(self):
        self.get_data()
y=Test(100)
y.get_data()
y.f1()
y.f2()
def new_data(self):
    print("taking the data from the test class")
Test.get_data=new_data
y.f2()
y.f1()

"""
#REGULAR EXPRESSION"""
#match
"""
import re
a="python is good"
y=re.match("python",a)
print(y)
"""
#full match
"""
import re
a="python is good"
y=re.fullmatch("python is good",a)
print(y)
"""
#search
""""
import re
a="python is good"
y=re.search(" g",a)
print(y)
"""
#sub and subn
"""
import re
x="good day"
y=re.sub("o","@",x,count=1)
print(y)

a="good day"
b=re.subn("o","@",x,count=1)
print(b)
"""
"""
import re
a="python is good"
y=re.match("y",a)
print(y)
"""
#match with start ,end,group
"""
import re
a="python is good"
y=re.match("python",a)
print(y)
print(y.start())
print(y.end())
print(y.group())
"""
#full match with start end group
"""
import re
a="python is good"
y=re.fullmatch("python is good",a)
print(y)
print(y.start())
print(y.end())
print(y.group())
"""
#1.matches any number between 0-9
"""
import re 
a="The cost of the book is Rs.100"
x=re.findall('[0-9]+',a)
print(x)
"""
#2.matches only lower case letter and upper case letter
"""
import re
b="hello HOW ARE YOU"

x=re.findall('[a-z]',b)
y=re.findall('[A-Z]',b)
print(len(y))
print(len(x))
print(x)
print(y)

"""
#3.write a program to count the number of white space in a given string
"""
import re
c="HELLO world welcome to python Hi how are you. Hi how are you"
x=re.findall('\s',c)
y=re.findall(" ",c)
print(len(x))
print(len(y))
"""
#4.sum all the numbers in the below string
"""
import re
word="PYTHON12nREG567exp2"
x=re.findall('[0-9]',word)
#print(x)
sum=0
for i in x:
    print(int(i))
    sum= sum+int(i)
print(sum)
"""
"""
#5.matches everything apart from numbers between 0-9
import re
a="The cost of the book is Rs.100"
x=re.findall('\D',a)
#y=re.match("x",a)
print(x)
"""
#6.matches everything apart from "a","b","c","d"
"""
import re
b="abcdefghijklmnop"
x=re.findall("[^abcd]",b)
print(x)
"""

#7.matches only those characters accepts digit
"""
import re
word="@hello12world34welcome!123"
x=re.findall("\D",word)
print(x)
"""

#8.extracting file with extension
"""
import re
s="Downloading archive.zip file to download folder python hero.py and afternoon.txt and slicing.jpeg"
x=re.findall("[a-z]+\.[a-z]+",s)
print(x)
"""
#9.wap to extract only pincode
"""
import re
s="Bangalore pincode is 560001 and area code is BSK234567 and state code is KAR123"
x=re.findall(r'[^A-Z]\d{6}',s)
print(x)
"""

#10.wap to print the AADHAR CARD numbers
"""
import re
s="my aadhar number is 1234-4567-8910"
x=re.findall(r'\d{4}-\d{4}-\d{4}',s)
print(x)
"""
#11.wap to print the pan card number
"""
import re
a="my pan number is ABCDE1234X and other number is PQRST5678W and id is 123abcd45"
x=re.findall('[A-Z]{5}\d{4}[A-Z]{1}',a)
print(x)
"""
#12.How to fetch the protocols
"""
import re
a="https://www.google.com"
x=re.findall('[a-z]+://+[a-z].+[a-z].+[a-z].+',a)
y=re.findall('[a-z]+',a)
print(y)
print(x)
"""
#13.creating acronyms of the file format
"""
import re
file_format=["Graphic Interchange Format", "Advanced Audio Coding",
            "HyperText Markup Language", "Content Management System",
          "Windows Media,Audio", "Comma Separated values"]
l1=[]

for i in file_format:
    x=" ".join(re.findall(r"\b(\w)",i.upper()))
    l1.append(x)
print(l1)

"""
#17.replace all digits with **
"""
import re
s="hello 123 mic testing 123 123"
x=re.subn('[0-9]',"**",s)
print(x)
"""

#16.replace whitespace with newline characters
"""
import re
s="helloworld welcome to python"
#x=re.findall(r"\s+","\n",s)
new=re.sub("\s","\n",s)
print(new)
"""

#14.wap to match email ids
"""
import re
emails=["test.user@company.gov","test_user@company.edu","123test-T.user@company.in",
        "testing@company","pspider@company.in"]
x=re.findall(r'[a-z]+\w+@+[a-z]+\.[a-z]{2,}',str(emails))
print(x)
"""
# for checking validation
"""
import re

emails = ["test.user@company.gov", "test_user@company.edu", "123test-T.user@company.in",
          "testing@company", "pspider@company.in"]


email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"

valid_emails = []
for email in emails:
  if re.match(email_regex, email):
    valid_emails.append(email)

print("Valid email addresses:")
print(*valid_emails, sep="\n")  # Print each email on a new line
"""
#15.matching phone numbers
"""
import re
phonenumbers=["123-345-0987","456-9832-098","800-987-4756","080-1029384727",
              "123-345-12","900-938-0987"]
match=re.findall('\d{3}-\d{3}-\d{4}',str(phonenumbers))
print(match)
"""
#13 again 
"""
import re
file_format=["Graphic Interchange Format", "Advanced Audio Coding",
            "HyperText Markup Language", "Content Management System",
          "Windows Media,Audio", "Comma Separated Values"]
for i in file_format:
    x=re.findall(r"[A-Z]",i)
    print((" ".join(x)))
"""






