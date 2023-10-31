class Solution:
    def summaryRanges(self, nums):
        
        fin=[]
        temp=[]

        while True:

            if len(nums)==0:
                break

            a=nums.pop(0)
            
            if temp:

                if temp[-1]+1==a:
                    temp.append(a)
                else:
                    if temp[0]!=temp[-1]:
                        s=f'{temp[0]}->{temp[-1]}'
                    else:
                        s=f'{temp[0]}'
                    fin.append(s)
                    temp=[]
                    temp.append(a)

            else:
                temp.append(a)
        if temp:
            
            if len(temp)==1:
                r=f"{temp[-1]}"
                fin.append(r)
            else:
                r=f"{temp[0]}->{temp[-1]}"
                fin.append(r)
        return fin