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
        targetSum -= root.val

        a = self.pathSum(root.left, targetSum)
        for lst in a:
            if len(lst)!=0:
                lst = [root.val]+lst
                ans.append(lst)
        a = self.pathSum(root.right, targetSum)
        for lst in a:
            if len(lst)!=0:
                lst = [root.val]+lst
                ans.append(lst)
        return ans

        