class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums=[1]+nums+[1]
        n=len(nums)
        dp=[[0]*n for _ in range(n)]
        for start in range(n-3,-1,-1):
            for end in range(start+2,n):
                for i in range(start+1,end):
                    now=dp[start][i]+nums[start]*nums[i]*nums[end]+dp[i][end]
                    dp[start][end]=max(dp[start][end],now)
        return dp[0][n-1]