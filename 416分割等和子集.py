#当数组的和为偶数时才有可能返回True
#类似于01背包
#设置状态转移方程dp[i][j]，表示数组0到i，是否有子集和为j
#情况1，当选取第i个数时dp[i][j]=dp[i][j-nums[i]]
#情况2，当不选取第i个数时dp[i][j]=dp[i-1][j]
#情况3，当nums[i]=j表示可以第i个数即可True
#需要考虑j与nums[i]的大小
#情况1，2，3为或的关系，即三者有一个为True即为True
from typing import List
class Solution1:
    def canPartition(self, nums: List[int]) -> bool:
        length=len(nums)
        s=sum(nums)
        if s%2!=0:
            return False
        else:
            target=s//2
        dp=[[False] * (target+1) for _ in range(length)]
        #初始化即数组第一个数的情况
        if nums[0]<=target:
            dp[0][nums[0]]=True
        for i in range(1,length):
            for j in range(target+1):
                dp[i][j]=dp[i-1][j]
                if nums[i]==j:
                    dp[i][j]=True
                elif nums[i]<j:
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-nums[i]]
        return dp[length-1][target]
#优化：
#1、由于dp数组中某个元素的值只与其上一行（i-1）的元素、上一行左边的元素相关
#则某一行如果dp[i][target]=True，则其下面的元素都为True，即直接可以返回True，复杂度不变，剪枝
#2、将dp二维数组优化为一维数组
class Solution2:
    def canPartition(self, nums: List[int]) -> bool:
        length=len(nums)
        s=sum(nums)
        if s%2!=0:
            return False
        else:
            target=s//2
        dp=[False]*(target+1)
        #初始化即数组第一个数的情况
        if nums[0]<=target:
            dp[nums[0]]=True
        for i in range(1,length):
            for j in range(target,nums[i]-1,-1):
                if dp[target]==True:
                    return True
                dp[j]=dp[j] or dp[j-nums[i]]
        return dp[target]