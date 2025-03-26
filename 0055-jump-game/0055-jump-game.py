class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i, jump in enumerate(nums):
            if i > max_reach:  # If current index is unreachable, return False
                return False
            max_reach = max(max_reach, i + jump)  # Update farthest reachable index
            if max_reach >= len(nums) - 1:  # If last index is reachable, return True
                return True
        return True      

        