import math
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        left=1
        right=max(piles)
        while left<right:
            mid=(left+right)//2
            if self.eatingTime(piles,mid)<=H:
                right=mid
            else:
                left=mid+1
        return left
    
    def eatingTime(self,piles,K):
        res=0
        for pile in piles:
            res+=math.ceil(pile/K)
        return res