class Solution:
    def maxDistance(self, colors: List[int]) -> int:


        max_dist=0

        color_list=set(colors)
        x=0

        for x in range(len(colors)-1):
            
         
            for y in range(x+1,len(colors)):

                if colors[x]!=colors[y]:

                    dis=abs(x-y)
                   

                    if dis>max_dist:
                        max_dist=dis
     

        return max_dist