# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root)->int:
        if not root:return 0
        else:
            return 1 + max(self.height(root.left), self.height(root.right))


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        else:
            if self.isBalanced(root.left) and self.isBalanced(root.right):
                left_height = self.height(root.left)
                right_height = self.height(root.right)
                if abs(left_height - right_height)<=1:
                    return True

        return False        
        