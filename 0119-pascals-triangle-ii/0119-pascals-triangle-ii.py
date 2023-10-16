import math
class Solution(object):
    def getRow(self, rowIndex):
        

        ar=[]
        for x in range(rowIndex+1):
            ar.append(math.comb(rowIndex,x))
        return ar