#Longest Substring without repeating characters

class Solution:
    def lengthOfLongestSubstring(self, s):


        if len(s)==0:
            return 0
            exit()
        elif len(s)==1:
            return 1
            exit()
        s1=[]
        l=[]
        for x in range(len(s)):

            l.append(len(s1))
            s1=[]
            for y in range(x,len(s)):

              if s[y] in s1:
                    l.append(len(s1))
                    break

              else:
                  s1.append(s[y])


        return(max(l))

q=Solution()
f=q.lengthOfLongestSubstring("au")
print(f)


