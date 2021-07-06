class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row=len(grid)
        col=len(grid[0])
        self.count=0
        acount=row*col
        self.parent=[-1]*acount
        self.rank=[0]*acount
        for i in range(row):
            for j in range(col):
                if grid[i][j]=="1":
                    idx=i*col+j
                    self.parent[idx]=idx
                    self.count+=1
                    if i>0 and grid[i-1][j]=="1":
                        nidx=(i-1)*col+j
                        self.connect(idx,nidx)
                    if j>0 and grid[i][j-1]=="1":
                        self.connect(idx,idx-1)
        return self.count

    def getparent(self,idx):
        if self.parent[idx]!=idx:
            return self.getparent(self.parent[idx])
        return idx
    def connect(self,p,q):
        rootp=self.getparent(p)
        rootq=self.getparent(q)
        if rootp!=rootq:
            if self.rank[rootp] < self.rank[rootq]:
                rootp, rootq = rootq, rootp
            self.parent[rootq] = rootp
            if self.rank[rootp] == self.rank[rootq]:
                self.rank[rootp] += 1
            self.count-=1