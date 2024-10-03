#mat.lib
#import matplotlib.pyplot as plt
#import numpy as np
#x=np.array([10,20])
#y=x**2
#x=[10,20,30]
#y=[10,20,30]
#plt.xlabel("x -axis")
#plt.ylabel("y-axis")
#plt.title("normal line graph")
#plt.plot(x,y,marker="o",mfc="r",mec="y",ms=20,ls="dashed" ,lw=30,color="y")
#plt.legend(loc="centre")
#plt.show()

""" bar graph"""
import matplotlib.pyplot as plt

a=["a","b","c","d","e"]
b=[70,30,90,10,50]
plt.xlabel("language")
plt.ylabel("ranking")
plt.title("full stack")
z=["r","y","c","m"]
plt.bar(a,b,lw=10,color=z,width=0.5,align="center",edgewidth=10,edgecolor="k")
plt.show()
"""
x=["python","java","c","c++"]
y=[95,85,75,65]
plt.xlabel("language")
plt.ylabel("ranking")
plt.title("full stack")
z=["r","y","c","m"]
plt.bar(x,y,lw=10,color=z,width=0.5,align="center")
plt.legend("info")
plt.show()

"""
