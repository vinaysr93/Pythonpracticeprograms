# Any or All

n=int(input())

ar=input().split()

if (all([int(x)>0 for x in ar])):

    print("Hello")
    print((any([m==m[::-1] for m in ar])))


else:
    print(False)