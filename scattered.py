import matplotlib.pyplot as plt
import numpy as np
"""
a=[10,80,56,47]
b=[50,34,71,80]
s=[12,13,14,15]
plt.xlabel("x value",fontsize=15)
plt.ylabel("y value",fontsize=15)
plt.title("scatter graph",fontsize=15)
plt.scatter(a,b ,sizes=s,color=['r','g','y','c'],marker="*",edgecolors="g",label="graph",alpha=0.25
            )
plt.colorbar()
plt.show()
"""
#using with numpy

l1=[]
for i in range(6):
    a=np.random.randint(500)
    #print(a)
    l1.append(a)
print(l1)
l2=[]
for i in range(6):
    b=np.random.randint(200)
    #print(a)
    l2.append(b)
print(l2)
l3=[]
for i in range(6):
    c=np.random.randint(100)
    #print(a)
    l3.append(c)
print(l3)
l4=[]
for i in range(6):
    d=np.random.randint(1000)
    #print(a)
    l4.append(d)
print(l4)
plt.scatter(l1,l2)
plt.scatter(l3,l4)
plt.scatter(l4,l1)
plt.scatter(l2,l4)
plt.scatter(l1,l4)
plt.show()

#stackplot
"""
s=[10,20,30,40]
t=[11,12,13,14]
u=[12,13,14,15]
v=[13,14,15,16]
q=["area1","area2","area3","area4"]
plt.stackplot(s,t,u,v,labels=q,colors=["r","m","c","b"])
plt.legend()
plt.show()
"""