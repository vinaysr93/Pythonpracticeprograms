# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:


        if len(nums)==1:
            root=TreeNode(nums[0])
            return root
        
        max_num= max(nums)

        root=TreeNode(max_num)
        self.tree_builder(root,nums)
        return root

    def tree_builder(self,root,arr):

        div_arr=self.tree_divider(arr)
        left_arr=div_arr[0]
        right_arr=div_arr[1]

        if left_arr:

            root.left=TreeNode(max(left_arr))
            self.tree_builder(root.left,left_arr)
            

        if right_arr:
            root.right=TreeNode(max(right_arr))
            self.tree_builder(root.right,right_arr)
            





    def tree_divider(self,arr):


        max_num= max(arr)
        index_max_num= arr.index(max_num)

        left_tree=arr[0:index_max_num]
        right_tree=arr[index_max_num:]
        right_tree.pop(0)

        return [left_tree,right_tree]
