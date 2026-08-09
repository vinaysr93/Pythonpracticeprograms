# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

       # val becomes the new root with the existing tree attached to its left.
        if not root or val > root.val:
            node = TreeNode(val)
            node.left = root
            return node

        # Otherwise, recurse down the right spine and attach the result back to root.right
        root.right = self.insertIntoMaxTree(root.right, val)
        return root