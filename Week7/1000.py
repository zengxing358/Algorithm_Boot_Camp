class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n=len(stones)
        if (n-1)%(k-1)!=0:
            return -1
        arr=[0]*(n+1)
        for i in range(n):
            arr[i+1]=arr[i]+stones[i]
        dp=[[float("inf")]*(n+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][i]=0
        for L in range(1,n+1):
            for left in range(1,n+1-L):
                right=left+L
                for step in range(left,right,k-1):
                    dp[left][right]=min(dp[left][right],dp[left][step]+dp[step+1][right])
                if L%(k-1)==0:
                    dp[left][right]+=arr[right]-arr[left-1]
        return dp[1][n]