#Codechef May long contest -https://www.codechef.com/MAY20B/problems/COVID19
t=int(input())

for x in range(t):

    n=int(input())
    r=list(map(int,input().split()))

    ct=[]
    count=1

    for y in range(len(r)-1):

        if r[y]+2>=r[y+1]:
            count=count+1

        else:
            ct.append(count)
            count=1
    ct.append(count)
    print(min(ct),max(ct))
