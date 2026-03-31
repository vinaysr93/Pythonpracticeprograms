class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        new_arr=[]
        count=0
        while(count<2):

            for x in range(len(nums)):
                new_arr.append(nums[x])
            
            count=count+1
        
        return new_arr
