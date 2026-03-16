# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        

        current=head #1
    

        count=1
        dummy = ListNode(0, head)
        prev=dummy
        reverse_count=right-left
        while current!=None:


            if count==left :

                for x in range(1,reverse_count+2):
                   if x==1:
                    actu_prev=prev #stores 1 here
                    new_pre=current # stores 2 here

                 
                   
                

                   nxt=current.next # nxt will be 3     #4 #5    
                   current.next=prev # 1 #2 #3
                   prev=current # previous will 2  #3 #4
                                                    
                   current=nxt  #3 #4 #5
                   
                   count=count+1 #3 #4 #5
                
                break

            prev=current # 1
            current=current.next # current is 2 
            count=count+1 # 2

        actu_prev.next=prev #1 points to 4
        new_pre.next=current #2 points to 5
                  
        return dummy.next