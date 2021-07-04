class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res=[]
        self.s='.'*n
        self.n=n
        self.solve(0,[],set(),set(),set())
        return self.res
    def solve(self,i,tmp,ns,xs,ys):
        if i==self.n:
            self.res.append(tmp)
            return
        for j in range(self.n):
            if j not in ns and i-j not in xs and i+j not in ys:
                self.solve(i+1,tmp+[self.s[:j]+'Q'+self.s[j+1:]],ns|{j},xs|{i-j},ys|{i+j})