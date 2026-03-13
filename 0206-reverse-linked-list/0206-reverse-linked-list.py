# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev=None
        current=head
       
       
        while current!=None:
            
            
            
            nxt=current.next # Points at 2
           
            current.next=prev #changes the pointer
            
            prev=current #1 becomes previous
           
            current=nxt #current becomes 2
           
        
        return prev