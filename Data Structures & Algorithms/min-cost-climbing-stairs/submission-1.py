class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[0]*(len(cost)-1)
        dp[0]=cost[0]
        dp[1]=cost[1]
        for i in range(2,len(cost)-1):
            dp[i]=min(cost[i]+dp[i-2],cost[i+1]+dp[i-1])
        return dp[-1]