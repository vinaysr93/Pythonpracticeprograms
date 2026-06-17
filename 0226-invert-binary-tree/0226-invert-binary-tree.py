# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        if root==None:
            return root

      
        self.helper(root)
        
        
        return root


    def helper(self,root):

        if ((root.left==None and root.right==None)):
           

            print(root.left)
            print(root.right)
            temp=root.left
            root.left=root.right
            root.right=temp
            print(root.left)
            print(root.left)
           
        elif root.left!=None and root.right!=None:

                
           
            self.helper(root.left)
            self.helper(root.right)
            
            temp=root.left
            root.left=root.right
            root.right=temp

        elif root.left==None:

             self.helper(root.right)
             temp=root.left
             root.left=root.right
             root.right=temp
        
        elif root.right==None:
             self.helper(root.left)
             temp=root.left
             root.left=root.right
             root.right=temp



            