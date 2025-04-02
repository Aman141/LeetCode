# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEqual(self,left, right):
        if not left and not right: return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
            
        return self.isEqual(left.right, right.left) and self.isEqual(left.left, right.right)
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        
        return self.isEqual(root.left,root.right)
        
        
        
        