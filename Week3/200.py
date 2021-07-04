class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        N=len(grid)
        M=len(grid[0])
        visit=[[False]*M for _ in range(N)]
        def bfs(i,j):
            visit[i][j]=True
            for x,y in [[i+1,j],[i-1,j],[i,j-1],[i,j+1]]:
                if x>=0 and x<N and y>=0 and y<M and grid[x][y]=='1' and not visit[x][y]:
                    bfs(x,y)
        res=0
        for i in range(N):
            for j in range(M):
                if grid[i][j]=='1' and not visit[i][j]:
                    bfs(i,j)
                    res+=1
        return res