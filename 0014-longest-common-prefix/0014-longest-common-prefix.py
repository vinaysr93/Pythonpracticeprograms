class Solution:
    def longestCommonPrefix(self, strs):
        
       sstrs=sorted(strs)
       print(sstrs)
       longest_prefix=[]
       
       if len(strs)==1:
           return "".join(strs)
        
       for x in range(len(sstrs[0])):

            t=sstrs[0][:x+1]
            print(t)
            counter=1
            for y in range(1,len(sstrs)):

                if sstrs[y].startswith(t):
                    counter=counter+1

                else:
                    break
            
            if counter==len(strs):
                longest_prefix.append(t)
            else:
                break
       if longest_prefix:
           print(longest_prefix)
           return "".join(longest_prefix[-1])
       else:
           return ""