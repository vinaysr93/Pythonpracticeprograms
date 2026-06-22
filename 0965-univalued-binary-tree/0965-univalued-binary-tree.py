# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        if root==None:
            return True
        root_val=root.val
        return(self.helper(root,root_val))

    
    def helper(self, root,root_val):

       if root==None:
        return True
       
       if root.val!=root_val:
        return False
    



       return (self.helper(root.left,root_val) and self.helper(root.right,root.val)) 