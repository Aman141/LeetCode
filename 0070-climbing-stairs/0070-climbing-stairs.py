class Solution:
    def climbStairs(self, n: int) -> int:

        ans = []
        ans.append(1)
        ans.append(2)    
        
        for i in range(2, n+1):
            ans.append(ans[i-1] + ans[i-2])

        return ans[n-1]    