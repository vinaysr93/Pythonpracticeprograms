#Reverse Integer Leet code


class Solution:
    def reverse(self, x):

        if x<0:
            a=str(x*-1)
            r=int(a[::-1])*-1

        else:
            a=str(x)
            r=(int(a[::-1]))

        if r>((pow(2,31)-1)) or r<(pow(-2,31)):
            return 0
        else:
            return r
s=Solution()
q=s.reverse(321)
print(q)