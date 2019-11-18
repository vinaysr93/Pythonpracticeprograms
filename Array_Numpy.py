import numpy


a=list(map(int,input().split()))
n=a[0]
m=a[1]
l1=[]
l2=[]
for x in range(n):

    l=list(map(int,input().split()))
    l1.append(l)

for y in range(n):
    q = list(map(int, input().split()))
    l2.append(q)
print(numpy.array((numpy.add(l1,l2))))
print(numpy.array((numpy.subtract(l1,l2))))
print(numpy.array((numpy.multiply(l1,l2))))
print(numpy.array((numpy.floor_divide(l1,l2))))
print(numpy.array((numpy.mod(l1,l2))))
print(numpy.array((numpy.power(l1,l2))))

