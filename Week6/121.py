class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        minnum=prices[0]
        maxpro=0
        for i in range(1,len(prices)):
            if prices[i]<minnum:
                minnum=prices[i]
            elif prices[i]-minnum>maxpro:
                maxpro=prices[i]-minnum
        return maxpro