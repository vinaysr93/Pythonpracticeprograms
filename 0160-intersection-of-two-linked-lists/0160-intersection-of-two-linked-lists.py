# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        dic={}

        #traversing through a
        while headA:
            if headA in dic:

                return headA
            
            else:

                dic[headA]=1
            
                headA=headA.next
        
        #traversing through b
        while headB:
            if headB in dic:
                return headB

            else:
                dic[headB]=1
                headB=headB.next

        return None