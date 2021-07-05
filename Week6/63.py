class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dic={}
        item=0
        for i in range(m):
            dic[(i,0)]=0
        while item<m:
            if obstacleGrid[item][0]!=1:
                dic[(item,0)]=1
                item+=1
            else:
                break
        for j in range(n):
            dic[(0,j)]=0
        item=0
        while item<n:
            if obstacleGrid[0][item]!=1:
                dic[(0,item)]=1
                item+=1
            else:
                break
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]!=1:
                    dic[(i,j)]=dic[(i-1,j)]+dic[(i,j-1)]
                else:
                    dic[(i,j)]=0
        return dic[(m-1,n-1)]


