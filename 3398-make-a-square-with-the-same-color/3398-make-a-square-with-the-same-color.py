class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:

        for i in range(2):
            for j in range(2):
                two_sq = [
                    grid[i][j], grid[i][j+1],
                    grid[i+1][j], grid[i+1][j+1]
                ]               
                if countOf(two_sq, "B") != 2: return True
        
        return False