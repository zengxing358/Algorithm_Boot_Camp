class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m,n=len(matrix),len(matrix[0])
        tmp=[[0]*(n+1) for i in range(m+1)]
        res=0
        for i in range(m):
            for j in range(n):
                tmp[i+1][j+1]=tmp[i][j+1]+tmp[i+1][j]+matrix[i][j]-tmp[i][j]
        for i in range(m):
            for ii in range(i+1,m+1):
                dic={}
                for j in range(n):
                    if (t:=tmp[ii][j+1]-tmp[i][j+1])==target:
                        res+=1
                    if (t-target) in dic:
                        res+=dic[t-target]
                    dic[t]=dic.get(t,0)+1
        return res
