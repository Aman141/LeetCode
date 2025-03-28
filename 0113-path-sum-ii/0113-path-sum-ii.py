# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return []
        if not root.left and not root.right:
            if root.val == targetSum:
                return [[root.val]]

        ans = []

        for tree in (root.left, root.right):
            a = self.pathSum(tree, targetSum-root.val)
            for lst in a:
                ans.append([root.val]+lst)

        return ans

        