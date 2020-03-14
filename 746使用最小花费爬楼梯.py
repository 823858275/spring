#dp[i]=min(dp[i-1],dp[i-2])+cost[i-2]
#表示最后一阶必须要走过时的最小的花费
#最后结果从倒数第一个与倒数第二个选一个
from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cur,pre=0,0
        for i in range(len(cost)):
            cur,pre=min(cur,pre)+cost[i],cur
        return min(cur,pre)
