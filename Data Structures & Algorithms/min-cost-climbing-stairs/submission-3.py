class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[0]*(len(cost)-1)
        dp[0]=cost[0]
        for i in range(1,len(cost)-1):
            dp[i]=min(dp[i-1]+cost[i],dp[i-2]+cost[i])
        return dp[-1]