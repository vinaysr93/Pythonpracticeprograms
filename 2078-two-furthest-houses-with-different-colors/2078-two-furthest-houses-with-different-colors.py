class Solution:
    def maxDistance(self, colors: List[int]) -> int:


        max_dist=0
        n=len(colors)
        color_list=set(colors)
        x=0

        for i  in range(len(colors)):

            if colors[i]!=colors[x]:
                max_dist=max(max_dist,i-x)

            if colors[n-1]!=colors[i]:
                max_dist=max(max_dist,n-1-i)
     

        return max_dist