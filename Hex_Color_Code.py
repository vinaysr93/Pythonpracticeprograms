#Hex Color Code

import re

n=int(input())

r=re.compile(r'#[0-9ABCDEFabcdef]{3,6}')
inside_braces=[]
valid=[]
contents=[]
for q in range(n):

    line=input().split()

    if line:
        contents.append("".join(line))


contents1="".join(contents)

for k in range(len(contents1)):

    if contents1[k]=='{' :
        pos1=k
    if contents1[k]=='}':
        pos2=k

        s="".join(contents1[pos1:pos2])
        valid.append((r.findall(s)))

for y in range(len(valid)):

     if len(valid[y])==0:
         continue
     else:
         for z in valid[y]:
             print(z)
