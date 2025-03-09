class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [triangle[0][0]]

        for i in range(1, len(triangle)):
            temp_dp = [num for num in triangle[i]]

            for j in range(len(triangle[i])):
                if j==0:
                        min_path = dp[0]

                elif j==len(triangle[i])-1:
                        min_path = dp[-1]

                else:
                    min_path = min(dp[j-1], dp[j])

                temp_dp[j] += min_path    
            dp = temp_dp

        return min(dp)

        



        