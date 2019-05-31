t=int(input())

for h in range(t):

    a1=input()
    a2=input()

    l=len(a1)
    ctr=0
    for x in range(l):
        if a1[x]=='?' and a2[x]=='?':
            continue
        elif a1[x]=='?' and a2[x]!='?':
            continue
        elif a2[x]=='?' and a1[x]!='?':
            continue
        elif a1[x]==a2[x]:
            continue
        else:
            ctr+=1
            break
    if ctr==1:
        print("No")
    else:
        print("Yes")


