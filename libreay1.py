"""
import numpy as np
import pandas as pd
dict1={"names":["saurabh","ajit","ali"],
       "marks":[12,45,67],
       "city":["nanded","hyderabad","yavatmal"]}
d=pd.DataFrame(dict1)
#print(d)
d.to_csv("friends.csv")
d.to_csv("friends2.csv",index=False)
x=d.head(1)
#print(x)
#print(d.tail(1))
#print(d.describe())
s=pd.read_csv("friends.csv")
#print(s)
s['marks'][0]=50
#print(x)
s.to_csv("friends.csv")
print(s)

"""
"""
#import numpy as np
import pandas as pd
name=["a","b","c","d"]
math=[56,67,78,87]
english=[45,78,90,67]
science=[78,90,34,78]
details={"names":name,"math":math,"english":english,"science":science}
x=pd.DataFrame(details , index=["i","ii","iii","iv"])
print(x)
data=x["total"]=0
print(data)
print(x)
data=x["total"]=x["math"]+x["english"]+x["science"]
print(x)

z=x.drop(columns="total")
print(z)

y=x.drop(index=["i"])
print(y)

#soreting
#w=x.sort_values("english",ascending=False)
#print(w
w=x.sort_values(["names","english"],ascending=[1,1])
print(w)
"""
import numpy as np
import pandas as pd
d=pd.DataFrame(np.random.rand(334,5))
#print(d)
#print(d.head(4))
#rint(d.tail(4)
#print(type(d.index))
#print(d.dtypes)     
#print(d.sort_index(axis=1,ascending=True))
#print(type(d[0]))
d.loc[0,0]=5656

d.columns=(list("abcde"))
d.loc[0,"a"]=565
#print(d.head())
d.loc[0,0]=678
d=d.drop(0,axis=1)
print(d.head(4))