import numpy as np
#copy method
x=np.array([1,2,3,4])
y=x
z=x.copy()
x[0]=23
print(x)
print(y)
print(z)

#indexing and slicing in array
a=np.array([11,12,13,14,15])
print(a.dtype)
print(a[2])
print(a[0:4:1])
b=np.array([[1,2,3,4,5],[2,4,5,6,7]])
print(b.ndim)
print(b[0][0])
print(b[[0][0:3:1]])

#travesing
"""
c=np.array([100,200,300])
for i in c:
    print(i)
c1=np.array([[1,2],[2,4]])
for k in c1:
    print(k)
for l in k:
    print(l)
    """

#how to join array
"""
d=np.array([2,6,7])
e=np.array([6,8,9])
e1=np.concatenate((d,e))
print(e1)
"""

#stack adding op-1d rowws but we can change the axis
"""
d=np.array([2,6,7])
e=np.array([6,8,9])
e1=np.stack((d ,e),axis=1)
print(e1)
print(e1.ndim)
"""
#vstack op-2d rows
"""

d=np.array([2,6,7])
e=np.array([6,8,9])
e1=np.vstack((d,e))
print(e1)
print(e1.ndim)
"""
#hstack op-2d
"""
d=np.array([2,6,7])
e=np.array([6,8,9])
e1=np.hstack((d,e))
print(e1)
"""
#dstack depth stack op-3d
"""
d=np.array([2,6,7])
e=np.array([6,8,9])
e1=np.dstack((d,e))
print(e1)
"""
#columstack op-2d in colums format
"""
d=np.array([2,6,7])
e=np.array([6,8,9])
e1=np.column_stack((d,e))
print(e1)
print(e1.ndim)
"""
#split
"""
s=np.array([[1,2,3,4,5,6],[5,6,7,8,9,0],[3,4,5,6,7,8]])
s1=np.split(s,3)
print(s1)

s=np.array([1,2,3,4,5,6])
s1=np.split(s,3)
print(s1)
"""
#searching number in array
"""
z=np.array([1,2,3,4,5,6])
z1=np.where(z==5)
print(z1)
"""
#intersection function
"""
z=np.array([1,2,3,4])
z1=np.array([5,4,7,8])
x=np.intersect1d(z,z1)
print(x)
#if no commen element then empty array
"""
#difference / uncommen elements
"""
z=np.array([1,2,3,4])
z1=np.array([5,4,7,8])
x=np.setdiff1d(z1,z)
x1=np.setdiff1d(z,z1)
print(x1)
print(x)
"""
#sort method
"""
z=np.array([5,2,9,0,2])
x=np.sort(z)
print(x)
"""
