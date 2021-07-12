import math
class Solution:
    def solveNQueens(self, n):
        self.res=[]
        self.s=[["."]*n  for  _ in range(n)]
        self.n=n
        self.size=(1<<n)-1
        self.solve(self.s[:],0,0,0,0)
        return self.res
    def solve(self,s,i,ns,xs,ys):
        if i>=self.n:
            self.res.append(["".join(t) for t in s])
            return
        can=self.size&(~(ns|xs|ys))
        while can!=0:
            temp=can&(-can)
            j=int(math.log2(temp))
            s[i][j]="Q"
            self.solve(s[:],i+1,ns|temp,(xs|temp)<<1,(ys|temp)>>1)
            s[i][j]="."
            can&=(can-1)