class Solution:
    def shuffle(self, nums, n):

        l=int(len(nums)/2)
        ar1=nums[0:l]
        ar2=nums[l:]
        ansar=[]

        for k in range(l):
            ansar.append(ar1[k])
            ansar.append(ar2[k])

        return ansar


s=Solution()

print(s.shuffle([2,5,1,3,4,7],3))