class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:

        dist_forward=0
        dist_backward=0
        i=startIndex
        n=len(words)
        flag=False
        while True:
            
            if words[i]==target:
               flag=True
               break
            
            else:
                i=((i+1+n)%n)
                dist_forward=dist_forward+1

            if dist_forward==n:
                break
            
            
        i=startIndex
        while True:

            if words[i]==target:
                flag=True
                break

            else:
                i=((i-1)%n)
                dist_backward=dist_backward+1
            
                if dist_backward==n:
                    break

        if flag==False:
            return -1
        
        return min(dist_forward,dist_backward)