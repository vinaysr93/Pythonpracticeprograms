# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
     #[1]
        
     
     
        slow=head
        fast=head
        flag=False

        while(fast and fast.next):
            flag=True
            prev=slow
            
            slow=slow.next
            slow_next=slow.next
            fast=fast.next.next

        if flag:
            prev.next=slow_next
            slow.next=None
        else:
            head=None

        return head