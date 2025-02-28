class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0 
        smallest= prices[0]
        for i in range(1, len(prices)):
            if prices[i]<smallest:
                smallest = prices[i]
            else:
                profit = prices[i]-smallest
                max_profit = max(profit, max_profit)

        return max_profit        


