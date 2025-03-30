# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        qu = [[root, False]]
        s = 0
        while qu:
            node = qu.pop(0)
            if node[1] and not node[0].left and not node[0].right :
                s += node[0].val

            else:
                if node[0].left:
                    qu.append([node[0].left, True])
                if node[0].right:
                    qu.append([node[0].right,False])   

        return s
        

        