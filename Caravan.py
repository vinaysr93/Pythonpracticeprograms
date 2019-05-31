#Caravans

t=int(input())

while(t>0):

    n=int(input())
    n2=list(map(int,input().split()))
    count=1
    mini=n2[0]
    for x in range(1,len(n2)):
        if n2[x]<mini:
            mini=n2[x]
            count=count+1

    print(count)
    t=t-1