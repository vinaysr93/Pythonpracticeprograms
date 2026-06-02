# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        

        if head==None:
            return head

        dummy= ListNode(-1)

        dummy.next=head
        nxt=head
        curr=dummy
      

        while nxt!=None:

            if nxt.val == val:
                nxt=curr.next.next
                curr.next=nxt
                continue

            curr=nxt
            nxt=curr.next

        return dummy.next