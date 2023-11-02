class Solution:
    def isSameAfterReversals(self, num):

        if num==0:
            return True
            
        s=str(num)
        ar=s[::-1]
        
        nr=ar.lstrip("0")
        rnr=nr[::-1]
        if rnr==s:
            return True
        else:
            return False
        
        