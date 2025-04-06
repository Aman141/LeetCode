# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def helper(root)->list:
            if not root:
                return []
            if not root.left and not root.right: return [[root.val]]

            ans = []

            left_tree = helper(root.left)
            right_tree = helper(root.right)

            for lst in left_tree:
                ans.append(lst + [root.val])

            for lst in right_tree:
                ans.append(lst + [root.val])

            return ans
        
        ans = helper(root)
        decimal_values = [int("".join(map(str, b[::-1])), 2) for b in ans]


        return sum(decimal_values)

        


            

        return 0

        