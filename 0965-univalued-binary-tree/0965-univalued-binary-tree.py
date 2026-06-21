# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        if root==None:
            return False
        root_val=root.val
        return(self.helper(root,root_val))

    
    def helper(self, root,root_val):

        if root.right!=None and root.left==None:

            if root.val==root_val:

                return self.helper(root.right,root_val)
            else:
                return False

        if root.left!=None and root.right== None:

            if root.val==root_val:

                return self.helper(root.left,root_val)
            else:
                return False

        
        if root.left!=None and root.right!= None:
            
            if root.val==root_val:
                return (self.helper(root.left,root_val) and self.helper(root.right,root_val))
                #left 1     # right 1
                #left 1     #returns True
                #returns true #returns true

            else:
                return False

        if root.left==None and root.right==None:

            return (root.val==root_val)

            