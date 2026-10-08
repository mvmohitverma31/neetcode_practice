class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev1=cost[0]
        prev2=cost[1]
        for i in range(2,len(cost)):
            dp=min(cost[i]+prev1,prev2)
            prev2=prev1
            prev1=dp
        return prev1