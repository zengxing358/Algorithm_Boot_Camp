class Solution:
    def maxProfit(self, prices, fee: int):
        n=len(prices)
        dp0=[0]*n
        dp1=[0]*n
        dp0[0]=-prices[0]
        for i in range(1,n):
            dp0[i]=max(dp1[i-1]-prices[i],dp0[i-1])
            dp1[i]=max(dp1[i-1],dp0[i-1]+prices[i]-fee)
        return dp1[-1]