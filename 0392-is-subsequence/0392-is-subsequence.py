class Solution:
    def isSubsequence(self, s: str, t: str) :
        count=0
        t_copy=t
        for a in s:

            if a in t_copy:
                r=t_copy.index(a);

                if r>=0:
                    
                    t_copy=t_copy[r+1:]
                    count+=1
                else:
                    return False
                
            
        if count==len(s):
            return True
        else:
            return False