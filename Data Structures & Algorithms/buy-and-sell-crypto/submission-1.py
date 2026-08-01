class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=0
        sell=1
        profit=0
        while sell<=len(prices)-1:
            if prices[sell]-prices[buy]>profit:
                profit=prices[sell]-prices[buy]
            elif prices[sell]-prices[buy]<=0:
                buy+=1
            sell+=1
        return profit