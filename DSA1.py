# fectorial or  diagrametical representition of execution ofg the program is called as flow chart
# linear search algorithem
"""
it is a searching algorithem which works onm a principle called sequential search,
where control will travese throungh each and every value present in a collection
one after the other  squential , to check weathwe the key is present or not.
"""
# steps to follow linear search algorithem
"""
step1- consider a list collection and a key to check
step2- start comparing the values from 0th index till len of the collection
step3-after getting the value same as key , return its index
step4- if key is not present then ignore
"""
# note
"""
in lineasr search algorithem if value is not present then also 
conmtrol will compare the values by performing n iteration 
to overcome this problem we are using we are using binary search algorithem
"""

# def linear_search(list,key):
    # for i in range(0,len(list)):
        # if key==list[i]:
            # print(i)
    # 
# linear_search([4,78,12,57,1,0],0)

# binary search
l=[1,2,3,4,5,6,7,8,9]
def binary_search(l,key):
    si=0
    ei=len(l)-1
    while si<=ei:
        mi=(si+ei)//2
        if key==l[mi]:
            return mi
        elif key>l[mi]:
            si=mi+1
        elif key<l[mi]:
            ei=mi-1
    
print(binary_search(l,key=7))
