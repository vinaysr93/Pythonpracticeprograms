#Birthday Cake Candles

n=int(input())

ar=list(map(int,input().split()))

k=max(ar)
ct=0
for x in range(n):
    if ar[x]==k:
        ct+=1

print(ct)