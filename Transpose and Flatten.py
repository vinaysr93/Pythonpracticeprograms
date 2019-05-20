#Transpose and Flatten

import numpy

n,m=map(int,input().split())

q1=[]


for x in range(n):


        q2=list(map(int,input().split()))
        q1.append(q2)

q3=numpy.array(q1)
print(q3.transpose())
print(q3.flatten())