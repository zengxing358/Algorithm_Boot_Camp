
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        dp=[0]*n
        dp[0]=nums[0]
        for i in range(1,n):
            if dp[i-1]>=i:
                dp[i]=max(dp[i-1],nums[i]+i)
        return dp[-1]>=n-1
