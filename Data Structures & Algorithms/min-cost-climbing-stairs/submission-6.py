class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[0]*(len(cost))
        dp[0]=cost[0]
        for i in range(1,len(cost)):
            dp[i]=cost[i]+min(dp[i-2],dp[i-1])
        return min (dp[-1],dp[-2])