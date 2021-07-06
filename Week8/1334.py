class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph={i:{} for i in range(n)}
        for s,e,w in edges:
            graph[s][e]=w
            graph[e][s]=w
        visit={i:{} for i in range(n)}
        queue=[(i,i,0) for i in range(n)]
        while queue:
            temp=[]
            for (s,e,t) in queue:
                if e not in visit[s]:
                    visit[s][e]=t
                    for nx in graph[e]:
                        if t+graph[e][nx]<=distanceThreshold:
                            temp.append((s,nx,t+graph[e][nx]))
                elif t<visit[s][e]:
                    visit[s][e]=t
                    for nx in graph[e]:
                        if t+graph[e][nx]<=distanceThreshold:
                            temp.append((s,nx,t+graph[e][nx]))
            queue=temp
        return sorted(visit.items(),key=lambda x:(len(x[1]),-x[0]))[0][0]