# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root):
        if not root:return 0,0

        curr_left_dia, left_height = self.helper(root.left)
        curr_right_dia, right_height = self.helper(root.right)

        max_dia = max(curr_left_dia, curr_right_dia, (left_height+ right_height))

        return max_dia, 1 + max(left_height, right_height)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        max_dia, height = self.helper(root)  

        return max_dia



        