from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp=[0]*(len(grid[0]))
        dp[0]=grid[0][0]
        for j in range(1,len(grid[0])):
            dp[j]=dp[j-1]+grid[0][j]
        for i in range(1,len(grid)):
            for j in range(len(grid[0])):
                if j==0:
                    dp[j]=dp[j]+grid[i][j]
                else:
                    dp[j]=min(dp[j],dp[j-1])+grid[i][j]
        return dp[-1]

print(Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]]))