class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_length = current_increasing = current_decreasing = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:  # Increasing sequence
                current_increasing += 1
                current_decreasing = 1  # Reset decreasing count
            elif nums[i] < nums[i - 1]:  # Decreasing sequence
                current_decreasing += 1
                current_increasing = 1  # Reset increasing count
            else:
                current_decreasing = 1
                current_increasing = 1
            max_length = max(max_length, current_increasing, current_decreasing)
        
        return max_length      




        