class Solution:
    def nthUglyNumber(self, n):

        if n==1:
            return 1

        un=[1]
        nu=1
        count=0
        while (count<n):

            m=min(un)
            a=m*2
            b=m*3
            c=m*5

            un.remove(m)

            if a not in un:
                un.append(a)

            if b not in un:
                un.append(b)
            if c not in un:
                un.append(c)
            count=count+1
        return(m)


s=Solution()
print(s.nthUglyNumber(1690))