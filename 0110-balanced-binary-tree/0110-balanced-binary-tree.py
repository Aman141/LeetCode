# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root):
        if not root:return True, 0
        else:
            is_bal_left, left_height = self.helper(root.left)
            is_bal_right, right_height = self.helper(root.right)
            if abs(left_height - right_height)<=1 and is_bal_left and is_bal_right:
                return True, 1 + max(left_height, right_height)

        return False, -1


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        else:
            a, b = self.helper(root) 
            return a     
        