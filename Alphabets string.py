nm=list(map(int,input().split()))
n=nm[0]#9
m=nm[1]#27
d='-'
ddot=".|."
s='WELCOME'
midn=(n-1)//2# 4
midm=(m-1)//2# 13
nmid2=midn
mmid2=0
a=1
for x in range(midn):

    print(d*(midm-1),end='')
    print(ddot*(2*x+1),end='')
    print(d*(midm-1),end='')

    midm=midm-(3)
    print()

print('-'*((m-7)//2),end='')
print(s,end='')
print('-'*((m-7)//2))


for y in range(nmid2-1,-1,-1):
    mmid2 = mmid2 + (3)
    print(d*(mmid2),end='')
    print(ddot*(2*y+1),end='')
    print(d*(mmid2),end='')


    print()