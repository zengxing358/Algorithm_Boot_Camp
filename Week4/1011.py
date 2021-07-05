class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left=max(weights)
        right=sum(weights)
        while left<right:
            mid=(left+right)//2
            if self.days(weights,mid)<=D:
                right=mid
            else:
                left=mid+1
        return left
    
    def days(self,weights,K):
        res=0
        temp=0
        for weight in weights:
            if temp+weight>K:
                res+=1
                temp=weight
            else:
                temp+=weight
        return res+1