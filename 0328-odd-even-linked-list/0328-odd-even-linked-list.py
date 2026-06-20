# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        if (head==None) or (head.next==None) or  (head.next.next==None):
            return head

        odd_head=head
        even_head=head.next
        odd_curr=head
        even_curr=even_head

        while(odd_curr.next!=None and even_curr.next!=None):
            
           odd_curr.next=odd_curr.next.next
           even_curr.next=even_curr.next.next

           odd_curr=odd_curr.next
           even_curr=even_curr.next

        odd_curr.next=even_head
            

        

        return head   