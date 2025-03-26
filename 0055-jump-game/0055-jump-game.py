class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[0] = True
        for i in range(len(nums)):
            if dp[i]:
                a = nums[i]
                if a >= (len(dp)-i):
                    return True

                dp[i+1:i+a+1] = [True]*a

        return dp[-1]        

        