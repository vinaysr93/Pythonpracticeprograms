# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        #palindrome reads same from reverse.
        # Reverse the linkedlist and get a confirmation

        dummy=ListNode(-1)
        copy_list=dummy
        current=head
        

        while (current):

           new_node=ListNode(current.val)
           copy_list.next=new_node

           current=current.next
           copy_list=copy_list.next 

     
        #1,1,2,1
        prev=None
        curr=dummy.next # 1
      
        while(curr):

            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
            
          
            
            
            
        curr=prev
        new_curr=head
        flag=True
        while (new_curr and curr):

            if curr.val==new_curr.val:
                curr=curr.next
                new_curr=new_curr.next
                continue
            else:
                flag=False
                break

        if flag==False:
            return False
        else:
            return True