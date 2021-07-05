class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not (prices and k):
            return 0
        dic={}
        L=len(prices)
        def dfs(n,t,frag):
            if (n,t,frag) in dic:
                return dic[(n,t,frag)]
            if t==0 or (n==0 and frag==0):
                return 0
            if n==0 and frag==1:
                return -prices[0]
            if frag==0:
                res=max(dfs(n-1,t,0),dfs(n-1,t,1)+prices[n])
            else:
                res=max(dfs(n-1,t,1),dfs(n-1,t-1,0)-prices[n])
            dic[(n,t,frag)]=res
            return res
        res=dfs(L-1,k,0)
        return res