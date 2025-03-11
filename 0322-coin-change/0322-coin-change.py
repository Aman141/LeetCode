class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for i in range(amount+1)]
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount+1):
                if dp[i-coin]!=float('inf'):
                        dp[i] = min(dp[i-coin] + 1, dp[i])  

        return dp[-1] if dp[-1]!= float('inf') else -1       

        