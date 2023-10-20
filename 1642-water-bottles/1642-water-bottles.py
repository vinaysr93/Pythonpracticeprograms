class Solution:
    def numWaterBottles(self, numBottles, numExchange):

        s=numBottles
        
        while(numBottles>=numExchange):
            
            r=numBottles%numExchange
            numBottles=numBottles//numExchange
            s=s+numBottles
            numBottles+=r
        return s