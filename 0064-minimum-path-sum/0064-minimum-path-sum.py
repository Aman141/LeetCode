class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Initialize a 2D DP table with zeros
        m = len(grid)
        n = len(grid[0])        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        # Set the first row and first column to 1 (Base case)
        dp[0][0] = grid[0][0]
        for i in range(1,m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1,n):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        # Fill the DP table using bottom-up approach
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j] , dp[i][j-1]) 


        return dp[m-1][n-1]  
        