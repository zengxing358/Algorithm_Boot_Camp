class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        L=len(nums)
        if L==1:
            return nums[0]
        premax=1
        premin=1
        res=-float("inf")
        for i in range(L):
            if nums[i]<0:
                premax,premin=premin,premax
            premax=max(premax*nums[i],nums[i])
            premin=min(premin*nums[i],nums[i])
            res=max(premax,res)
        return res
