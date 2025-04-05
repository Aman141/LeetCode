# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2: return True
        def inorderleaf(root):
            if not root: return []
            if not root.left and not root.right: return [root.val]
            ans = []
            ans+= inorderleaf(root.left)
            ans+= inorderleaf(root.right)

            return ans

        ans_1 = inorderleaf(root1)
        ans_2 = inorderleaf(root2)
        return ans_1==ans_2


        