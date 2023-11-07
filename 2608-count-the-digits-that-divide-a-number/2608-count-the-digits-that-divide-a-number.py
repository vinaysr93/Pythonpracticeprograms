class Solution:
    def countDigits(self, num):

        s=str(num)
        count=0
        for x in s:

            a=int(x)
            if num%a==0:
                count=count+1
        
        return count
        