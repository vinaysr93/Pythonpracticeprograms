class Solution:
    def firstUniqChar(self, s):

        count={}
        for chr in s:
            if chr in count:
                count[chr]=count[chr]+1
            else:
                count.setdefault(chr,1)


        for j in count.keys():

            if count[j]==1:
                print(s.index(j))
                exit()


        print(-1)
e=Solution()
e.firstUniqChar("aadadaad")