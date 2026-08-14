class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        

        max_length=0
        for x in range(len(s)):

            for a in range(len(s)):

                i=self.str_count(s[x:a+1])
               
                if i:
                    if len(s[x:a+1])>max_length:
                        max_length=len(s[x:a+1])
                
        return max_length
    


    def str_count(self,s):


        dic={}
        for a in s:

            if a in dic:
                dic[a]=dic[a]+1
                if dic[a]>2:
                    return False
            
            else:
                dic[a]=1
        
        
        return True