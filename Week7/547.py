class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        graph={n:set() for n in range(len(M))}
        visit=set()
        for i in range(len(M)):
            for j in range(len(M)):
                if i!=j and M[i][j]==1:
                    graph[i].add(j)
        def bfs(index):
            for nextindex in graph[index]:
                if nextindex not in visit:
                    visit.add(nextindex)
                    bfs(nextindex)
        res=0
        for i in range(len(M)):
            if i not in visit:
                visit.add(i)
                res+=1
                bfs(i)
        return res

