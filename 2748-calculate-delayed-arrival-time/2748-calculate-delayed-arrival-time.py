class Solution:
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):

        a=arrivalTime+delayedTime
        if a>=24:
            a=a%24
        
        return a 
        