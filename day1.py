import numpy as np
print(np.__version__)
a=[1,2,3,4,10+2j]
b=("a","b",1)
x=np.array(a)
z=np.array(b)
print(x)
print(z)
c=np.array(100)
print(type(c))
c1=np.array([[[100,200,400],[1,2,3],[2,4,5]]])
print(c.ndim)
print(c1)
print(c1.ndim)
d=np.arange(1,10,2)
print(d)
print(d.ndim)
print(c1.reshape(3,3))
e=np.array([1,2,3,4,5,6])
print(c1.shape)
e1=np.array([[[1,2,3,4,5],[2,4,5,6,7],[4,5,6,67,8]]])
print(e1.reshape(3,5))
f=np.linspace(1,10,4,retstep=True)
print(f)

#once
f1=np.ones((2,2))
print(f1)
print(f1.ndim)
print(f1.dtype)
print(type(f1))

#zeros
f2=np.zeros((4,2))
print(f2)
print(f2.dtype)
print(f2.ndim)
#diagonal / identity
g=np.identity(3)
print(g)
print(g.dtype)
print(g.ndim)

#copy



"""
list - collection of hogrnous and hetrogrnious data items
more comlpex
more memory consumption
limited operations can be performed on a list
discontious memory allocation
list operation will be slower


array -  collection of homogenous data items
less complex
less memory consumtion
multiple operation can be perfotmed on a array
continous memory allocation
array operations will be faster
"""


"""
range- when we are using yhe range fun it is requried to do typecastiong to get the proper o/p
it can only create int value between the given range
create squence of int number between the the given range of the number


arange-
no need of typevcasting
it will giving int as well as float values
create an array between the range of given number
"""