from copy import deepcopy
m=[1,3,7,9]
n=deepcopy(m)
m[1]=34
n[3]=35
print(m)
print(n)
print(id(m))
print(id(n))