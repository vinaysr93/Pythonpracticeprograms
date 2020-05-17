class Solution:
    def twoSum(self, nums, target):

        for x in range(len(nums)):

            for y in range(x+1,len(nums)):

                if nums[x]+nums[y]==target:
                    ar=[x,y]
                    break

        return (ar)

s=Solution()
r=s.twoSum([2, 7, 11, 15],9)
print(r)