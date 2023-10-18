class Solution(object):
    def constructRectangle(self, area):
     
     ar=int(math.sqrt(area))
     minimum_diff=100000000000
     r=[]
     for x in range(ar,0,-1):
         if area%x==0:
             return [area//x,x]