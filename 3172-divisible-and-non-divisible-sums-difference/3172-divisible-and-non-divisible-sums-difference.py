class Solution:
    def differenceOfSums(self, n, m):

        num1=0
        num2=0
        for x in range (1,n+1):
            if x%m==0:
                num2=num2+x
            else:
                num1=num1+x

        return num1-num2
        