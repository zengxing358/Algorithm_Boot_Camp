class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)
        dp=[[1]*n for _ in range(n)]
        for l in range(2,n+1):
            for left in range(n-l+1):
                right=left+l-1
                if s[left]==s[right]:
                    if l==2:
                        dp[left][right]=2
                    else:
                        dp[left][right]=dp[left+1][right-1]+2
                else:
                    dp[left][right]=max(dp[left+1][right],dp[left][right-1])
        return dp[0][n-1]