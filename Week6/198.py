class Solution:
    def rob(self, nums: List[int]) -> int:
        dp1=0
        dp2=0
        for i in range(len(nums)):
            dp1,dp2=dp2,max(dp2,dp1+nums[i])
        return dp2