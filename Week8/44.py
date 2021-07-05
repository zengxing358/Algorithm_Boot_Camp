class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        l1=len(s)
        l2=len(p)
        dp={(i,0):False for i in range(1,l1+1)}
        dp[(0,0)]=True
        for j in range(1,l2+1):
            if p[j-1]=='*':
                dp[(0,j)]=dp[(0,j-1)]
            else:
                dp[(0,j)]=False
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                if s[i-1]==p[j-1] or p[j-1]=='?':
                    dp[(i,j)]=dp[(i-1,j-1)]
                elif p[j-1]=='*':
                    dp[(i,j)]=dp[(i-1,j)] or dp[(i,j-1)]
                else:
                    dp[(i,j)]=False
        return dp[(l1,l2)]