# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if self.checkMirror(root.left,root.right):
            return True
        else:
            return False

    def checkMirror(self,node1,node2):

        if node1==None and node2==None:
            return True

        elif node1==None or node2==None:
            return False

        elif node1!= None and node2!=None:
            
            if (self.checkMirror(node1.left,node2.right) and  self.checkMirror(node1.right,node2.left)):
            
            
            
                        
                    if node1.val == node2.val:
                                    return True
                    else:
                                    return False
     