from functools import lru_cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.graph={}
        deg={}
        row=len(matrix)
        self.col=len(matrix[0])
        num=row*self.col
        for i in range(row):
            for j in range(self.col):
                idx=self.getcode(i,j)
                if i+1<row and matrix[i][j]!=matrix[i+1][j]:
                    nidx=self.getcode(i+1,j)
                    if matrix[i][j]>matrix[i+1][j]:
                        self.graph[nidx]=self.graph.get(nidx,[])+[idx]
                        deg[idx]=deg.get(idx,0)+1
                    else:
                        self.graph[idx]=self.graph.get(idx,[])+[nidx]
                        deg[nidx]=deg.get(nidx,0)+1
                if j+1<self.col and matrix[i][j]!=matrix[i][j+1]:
                    nidx=self.getcode(i,j+1)
                    if matrix[i][j]>matrix[i][j+1]:
                        self.graph[nidx]=self.graph.get(nidx,[])+[idx]
                        deg[idx]=deg.get(idx,0)+1
                    else:
                        self.graph[idx]=self.graph.get(idx,[])+[nidx]
                        deg[nidx]=deg.get(nidx,0)+1
        hold={i for i in range(num)}-deg.keys()
        self.res=0
        for node in hold:
            self.dfs(node,1)
        return self.res
    @lru_cache(None)
    def dfs(self,node,idx):
        if node in self.graph:
            for nxt in self.graph[node]:
                self.dfs(nxt,idx+1)
        else:
            self.res=max(self.res,idx)
    def getcode(self,x,y):
        return x*self.col+y