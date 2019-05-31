# Binary Shuffle

t=int(input())

for i in range(t):

    a,b=map(int,input().split())
    if a==b:
        print(0)
    elif b==0:
        print(-1)
    elif b==1:
        if a==0:
            print(1)
        else:
            print(-1)
    else:
        a1=bin(a)
        ac=a1.count('1')
        b1=bin(b-1)
        bc=b1.count('1')

        if ac==bc:
            print(1)
        elif ac<bc:
            print((bc-ac)+1)
        elif ac>bc:
            print(2)

