class Solution:
    def numWaterBottles(self, numBottles, numExchange):

        s=numBottles
        q=numBottles//numExchange
        r=numBottles%numExchange
        s=s+q
        num=q+r
        while(num>=numExchange):
            
            q=num//numExchange
            print("Q",q)
            r=num%numExchange
            print("R",r)
            s=s+q
            print("Sum",s)
            num=q+r
        return s