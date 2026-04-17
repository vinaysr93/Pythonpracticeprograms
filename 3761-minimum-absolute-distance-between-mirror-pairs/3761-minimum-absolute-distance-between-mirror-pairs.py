import math
class Solution:
    
    
    def reverseNumber(self,num):

        #110
        s=str(num)[::-1]
        n=int(s)

        return n

    
    def minMirrorPairDistance(self, nums: List[int]) -> int:

        dic={}


        for x in range(len(nums)):

            if nums[x] in dic:

                dic[nums[x]].append(x)
            
            else:
                dic[nums[x]]=[x]
            
        print (dic)
        diff= math.inf
        not_present=[]
        for x in range(len(nums)):
            
            rev_num=self.reverseNumber(nums[x])
            if rev_num in dic:

                ar=dic[rev_num]

                for m in ar:

                    if m>x:
                    
                        d=abs(m-x)
                        if d<diff:
                            diff=d
                
                if diff==1:
                    break
        
        if diff==math.inf:
            return -1
               
        return diff
    


        