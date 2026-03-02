class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for x in range(len(nums)):

           diff=target-nums[x]

           if diff in nums and nums.index(diff)!=x:
                return [x,nums.index(diff)]