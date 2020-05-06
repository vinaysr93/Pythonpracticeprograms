class Solution:
    def majorityElement(self, nums):

        count={}
        m=0
        for x in nums:
            if x in count:
                count[x]+=1

            else:
                count.setdefault(x,1)

        key_list=list(count.keys())

        value_list=list(count.values())

        print(key_list[value_list.index(max(value_list))])


e=Solution()
e.majorityElement([3,2,3])


# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         # majority element is the element that appears more
#         # than n/2 times
#
#         nums.sort()
#
#         majority = nums[int(len(nums) / 2)]
#         return majority