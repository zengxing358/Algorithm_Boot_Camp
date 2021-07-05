class Solution:
    def longestPalindrome(self, s: str) -> str:
        L=len(s)
        if L<=1:
            return s
        dp=[[False]*L for _ in range(L)]
        res=s[0]
        cnt=1
        for i in range(1,L):
            for j in range(i):
                if i-j<=2:
                    if s[i]==s[j]:
                        dp[i][j]=True
                        cur_len=i-j+1
                else:
                    if s[i]==s[j] and dp[i-1][j+1]:
                        dp[i][j]=True
                        cur_len=i-j+1
                if dp[i][j]:
                    if cur_len>cnt:
                        cnt=cur_len
                        res=s[j:i+1]
        return res