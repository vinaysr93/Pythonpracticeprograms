# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        l=[]

        current=head
      
        count=0

        while (current!=None):

            l.append(current)
            count=count+1
            current=current.next
            

      

        mid=count//2
        new_count=0
        new_current=head
        while (new_count<=mid-1):

            new_current=new_current.next
            new_count=new_count+1
        return new_current