class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1:
            return -1
        res=0
        N=len(grid)
        M=len(grid[0])
        queue=[(0,0)]
        visit=set()
        while queue:
            temp=[]
            res+=1
            for x,y in queue:
                if x==N-1 and y==M-1:
                    return res
                for nx,ny in [(x-1,y),(x-1,y-1),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]:
                    if nx>=0 and nx<N and ny>=0 and ny<M and grid[nx][ny]==0 and ((nx,ny) not in visit):
                        temp.append((nx,ny))
                        visit.add((nx,ny))
            queue=temp
        return -1

