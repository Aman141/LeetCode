# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(root,val):
            if not root.left and not root.right: return val

            val_left = 0
            val_right = 0

            if root.left:
                val_left = helper(root.left, 10*val + root.left.val)

            if root.right:
                val_right = helper(root.right, 10*val + root.right.val)    

            return val_left + val_right
        if not root: return 0
        return helper(root,root.val)
        


        