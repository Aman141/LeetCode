# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        def helper(root):
            if not root: return 0, 0
            if not root.left and not root.right: return 0, root.val

            left_tree_tilt, left_tree_sum = helper(root.left)
            right_tree_tilt, right_tree_sum = helper(root.right)
            return left_tree_tilt + right_tree_tilt + abs(right_tree_sum- left_tree_sum), (right_tree_sum + left_tree_sum + root.val)


        return helper(root)[0]    


        