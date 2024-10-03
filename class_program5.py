"""
#1
num=2
if num%2==0:
    print("even")
    if num>5:
        print(f"{num} is greater than 5")
    else:
         print(f"{num} is not\ greater than 5")
else:
    print("odd")
    
"""
"""
#2
n=35
if n%2==1:
    print("odd")
    if n%7==0:
        print(f"{n} is divisable by 7" )
    else:
        print(f"{n} is not divisable by 7" )
else:
    print("even")
"""
"""
#3
n=33
if n%2==1:
    print("odd")
    if n%7==0:
        print(f"{n} is divisable by 7" )
    else:
        print(f"{n} is not divisable by 7" )
else:
    p"rint("even")
"""
"""
#4
u=input("enter username")
p=input(" enter password")
if u=="python" and p=="python masters":
    print("login succefully")
else:
    print("login failed")
    """
"""
#5
t=eval(input("theater name"))
theather=["pvr","esqure"]
movies={"thor":200,"spiderman":120,"hulk":180}
if t in theather:
    m=eval(input('enter movie name'))
    if m in movies:
        print("movie is avaliable")
        price=movies.get(m)
        print(f"{m} price is rs  {price}")
        print("tickect booked")

    else:
        print("movie is not avaliable")

else:
    print("sorry theater not avaliable")
    
 

    """
"""
#6
s=[3,4,6,7,9,1,5]
m1=len(s)
m2=m1//2
mid=s[m2]
if mid%2==0:
    print(f"middle number {mid} is even")
else:
    print(f"middle number {mid} is odd")
    """
"""
#7
apps=["flipkart","amazon"]
categories=["electronics","mobile","fashion","furnitures"]
phones={"oneplus","redmi","xami","motorola","iphone"}
a=input("enter app")
if a in apps:
    print(f"you are on {a}")
    b=input("enter catager")
    if b in categories:
        print(f"you have selected{b} catagery now we only havw phones")
        c=input("enter which brand phonme do you want to purchase")
        if c in phones:
            print(f"we have {c} brand phone")
            print("do you want to conmform booking")
            d=input("enter yes or no")
            if d=="yes":
                print("booking succcefuly")
            else:
                print("booing cancle")
        else:
            print("we dont have this phone in stock")
    else:
        print("categery is not avaliable")
    
else:
    print("sorry shopping app is not avaliable")

    """
"""
Product={"phone":15000,"salt":100, "pen":250,"sugar":500}
p1=eval("enter product 1")
p2=eval("enter product 2")
p3=eval("enter product 3")
"""
#8
mode=input("enter the mode of purchasing")
if mode=="credit card":
    no_of_products=int(input("enter number of products"))
    p1=eval(input("enter produc1 1"))
    p2=eval(input("enter produc1 2"))
    p3=eval(input("enter produc1 3"))
    
    if no_of_products>=3:
        #print("you have a chance to get 10% disscount")
        total=p1+p2+p3
        if total>=500:
            discount=10/100*total
            price=total-discount
            print(f"total price of product is {total} rs and after applying disscount it will be {price} rs ")
    else:
        print("no disscount")
        
else:
    print("no disscount")
