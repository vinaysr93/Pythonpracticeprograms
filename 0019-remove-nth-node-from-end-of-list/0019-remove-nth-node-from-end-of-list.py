# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #removing nth node from the list
        #edge cases- single element in the list
        #finding the nth element from the end.
        #count the number of elements
        #nth element from the end is total_elements-n+1 th element from the start.

        count=0
        current=head
        while(current):
            current=current.next
            count=count+1
        
        le=count
        op=le-n+1

        if le==1 and n==1:
            head=None
            return head

        new_current=head
        new_count=1
       
        if le==n:
            head=head.next
            return head

        while(new_current.next): # Checks 2 ,3,4, # 2
 
             prev=new_current  # Prev - 1,2,3, # 1
             new_current=new_current.next # new _crrent - 2,3,4 #2
             nxt=new_current.next #nxt= 3,4,5 #None
             new_count=new_count+1   # 1,2,3
             
             if new_count==op:
                prev.next=nxt
                break

             
        return head