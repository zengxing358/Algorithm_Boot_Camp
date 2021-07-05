class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp0=[-prices[0]]
        dp1=[0]
        for i in range(1,len(prices)):
            dp1.append(max(dp1[i-1],prices[i]+dp0[i-1]))
            dp0.append(max(dp1[i-2]-prices[i],dp0[i-1]))
        return dp1[-1]