# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
       count=0
       dic={}
       flag=True

       # Handles when its an empty list or a list with only one element
       if not head or not head.next:
            return None
        
       curr_ele=head
       dic[curr_ele]=count
       

       while curr_ele.next is not None:

            curr_ele=curr_ele.next

            if curr_ele in dic:
                
                flag=False
                return curr_ele
                
              

            else:
                count=count+1
                dic[curr_ele]=count

       if flag:

            return None
        
            