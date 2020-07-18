class Solution:
    def runningSum(self, nums) :

        l=len(nums)
        ar=[]
        for x in range(l):

            s=sum(nums[0:x+1])
            ar.append(s)

        return ar



q=Solution()
print(q.runningSum([1,2,3,4]))
