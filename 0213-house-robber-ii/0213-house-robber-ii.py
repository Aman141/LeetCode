class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)
        dp_1 = []
        dp_1.append(nums[0])
        dp_1.append(max(nums[0],nums[1]))
        for i in range(2, len(nums)-1):
            dp_1.append(max(dp_1[i-2]+nums[i], dp_1[i-1]))

        dp_2 = []
        dp_2.append(nums[1])
        dp_2.append(max(nums[1],nums[2]))
        for i in range(2, len(nums)-1):
            dp_2.append(max(dp_2[i-2]+nums[i+1], dp_2[i-1]))

        return max(dp_2[-1], dp_1[-1])    
        