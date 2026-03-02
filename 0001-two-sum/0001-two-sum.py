class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ind={}
        

         

        for k in range(len(nums)):

            diff=target-nums[k]

            if diff in ind:
                return [k,ind[diff]]

            else:
                ind[nums[k]]=k