#Shape and Reshape

import numpy
n=list(map(int,input().split()))

q1=numpy.array(n)
q2=numpy.reshape((q1),(3,3))
print(q2)