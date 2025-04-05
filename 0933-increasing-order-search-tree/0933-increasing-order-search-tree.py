# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dummy = TreeNode(0)
        curr_node = dummy

        st = []
        curr = root
        ans = None
        lst = []
        while st or curr:
            while curr:
                st.append(curr)
                curr= curr.left
            node = st.pop()
            curr_node.right = TreeNode(node.val)
            curr_node = curr_node.right
            
            curr = node.right
  
        
        return dummy.right

        