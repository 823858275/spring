from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp=[0]*len(triangle)
        for i in range(len(triangle)):
            for j in range(len(triangle[i])-1,-1,-1):
                if j==0:
                    dp[j]=dp[j]+triangle[i][j]
                elif j==len(triangle[i])-1:
                    dp[j]=triangle[i][j]+dp[j-1]
                else:
                    dp[j]=min(dp[j]+triangle[i][j],dp[j-1]+triangle[i][j])
        return min(dp)
