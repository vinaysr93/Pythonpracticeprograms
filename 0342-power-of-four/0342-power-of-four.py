import math
class Solution:
    def isPowerOfFour(self, n):


        if n<=0:
            return False
        else:
            a=math.log(n,4)
            b=math.log(4,4)
            print(a,b)
            if a%b==0:
                return True
            else:
                return False        