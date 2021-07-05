class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        count=0
        l=len(prices)
        i=0
        while True:
            for j in range(i,l-1):
                if prices[j+1]>prices[j]:
                    count+=prices[j+1]-prices[j]
                else:
                    i=j
                    break
            else:
                break
            i+=1
        return count