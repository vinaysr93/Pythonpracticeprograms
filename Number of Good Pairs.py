import math
class Solution:


    def numIdenticalPairs(self, nums):

        l=len(nums)

        count={}


        for x in nums:

            if x in count:
                count[x]+=1

            else:
                count.setdefault(x,1)


        s=0
        for j in count.values():

            if j>1:

             s=s+(math.factorial(j))/(math.factorial(j-2)*2)

        return s
q=Solution()
print(q.numIdenticalPairs([1,2,3,1,1,3]))