class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Initialize a 2D DP table with zeros
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        # Set the first row and first column to 1 (Base case)
        obstacle_row = False
        obstacle_column = False
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                dp[i][0] = 0
                obstacle_row = True
                continue
            elif obstacleGrid[i][0] == 0 and obstacle_row :
                dp[i][0] = 0
                continue
            dp[i][0] = 1

        for j in range(n):
            if obstacleGrid[0][j] == 1:
                dp[0][j] = 0
                obstacle_column = True
                continue
            elif obstacleGrid[0][j] == 0 and obstacle_column :
                dp[0][j] = 0
                continue
            dp[0][j] = 1
        # Fill the DP table using bottom-up approach
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j]==1:
                    dp[i][j] = 0
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]  
        return dp[m-1][n-1]  
        