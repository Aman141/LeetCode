# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: return []
        from collections import deque
        ans = []
        qu = [root]
        while qu:
            s = 0
            l = len(qu)
            for i in range(l):
                node = qu.pop(0)
                s += node.val
                if node.left:
                    qu.append(node.left)
                if node.right:
                    qu.append(node.right)

            ans.append(s/l)

        return ans    


        