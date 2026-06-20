# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        

        curr=head
        po=0
        ar=[]
        while (curr!=None):
            ar.append(curr.val)
            curr=curr.next
        print(ar)
        for x in range(0,len (ar)):
            po=po+ar[x]*math.pow(2,(len(ar)-x-1))
        
        return int(po)



