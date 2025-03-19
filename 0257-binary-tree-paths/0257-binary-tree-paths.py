# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        ans = []
        str_left = self.binaryTreePaths(root.left)
        str_right = self.binaryTreePaths(root.right)
        if len(str_left) == 0 and len(str_right)==0:
            a = f"{root.val}"
            ans.append(a)
        else:
            for i in str_right:
                b = f"{root.val}->" + i
                ans.append(b)

            for j in str_left:
                a = f"{root.val}->" + j
                ans.append(a)
        
        return ans
