#apples and oranges
#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):


    house=[num for num in range(s,t+1)]
    c_a=0
    c_o=0
    #apples

    for x in range(len(apples)):

        if(apples[x]+a)>=s and (apples[x]+a)<=t:
            c_a+=1

    for y in range(len(oranges)):
        if (oranges[y]+b) >=s and (oranges[y]+b)<=t:
            c_o+=1


    print(c_a)
    print(c_o)
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])# starting point of sams location

    t = int(st[1])# ending point of sams location

    ab = input().split()

    a = int(ab[0])#location of apple tree

    b = int(ab[1])# location of orange tree

    mn = input().split()

    m = int(mn[0])#number of apples

    n = int(mn[1])#number of oranges

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
