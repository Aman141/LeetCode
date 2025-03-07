class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a 2D DP table with zeros
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        # Set the first row and first column to 1 (Base case)
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        # Fill the DP table using bottom-up approach
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]  # Sum of top and left cells

        return dp[m-1][n-1]  # Return the number of unique paths to bottom-right


        