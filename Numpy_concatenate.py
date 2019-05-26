#concatenate

import numpy

n,m,p=list(map(int,input().split()))


ar1=[]
ar2=[]
for x in range(n):

    art1=list(map(int,input().split()))
    ar1.append(art1)

for y in range(m):

    art2=list(map(int,input().split()))
    ar2.append(art2)


print(numpy.concatenate((ar1,ar2),axis=0))