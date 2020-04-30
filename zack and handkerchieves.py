
#Code chef Problem https://www.codechef.com/LRNDSA05/problems/ZACKHAN
t=int(input())


def gcd(a, b):
    # Everything divides 0
    if (a%b == 0):
        return b
    return gcd(b, a % b)

for x in range(t):

    m,n=(input().split())
    m=int(m)
    n=int(n)
    g=gcd(m,n)
    print(g)