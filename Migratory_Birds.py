# Migratory Birds

n=int(input())

ar=sorted(list(map(int,input().split())))
max_count=0
bird_id=0
count={}
for i in ar:

    count.setdefault(i,0)
    if i in count:
        count[i]+=1

        if count[i]>max_count:
            max_count=count[i]
            bird_id=i
print(bird_id)