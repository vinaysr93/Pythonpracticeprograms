c=int(input())


while(c>0):

    n=list(map(int,input().split())) # two numbers which have been input
    
    s=0
    t=n[1]
    for x in range(n[0]):
        s=0
        for y in range(t+1):

            s=s+y
        t=s

    print(s)
    c=c-1


