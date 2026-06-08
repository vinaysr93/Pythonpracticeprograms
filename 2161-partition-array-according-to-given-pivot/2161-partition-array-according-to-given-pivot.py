class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        less_than=[]
        equal_to=[]
        greater_than=[]


        for x in range(len(nums)):
            if nums[x]<pivot:
                less_than.append(nums[x])

            elif nums[x]>pivot:
                greater_than.append(nums[x])

            else:
                equal_to.append(nums[x])

        final=less_than+equal_to+greater_than

      
       
        print(final)

        return final