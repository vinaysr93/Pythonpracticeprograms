from itertools import permutations


s=input().split()

n=int(s[1])
word=s[0]
q1=sorted(list(word))

r=(list(permutations(q1,n)))


for x in range(len(r)):

    print("".join(r[x]))