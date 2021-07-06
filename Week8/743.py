class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph={i:{} for i in range(1,n+1)}
        for s,e,t in times:
            graph[s][e]=t
        visit={}
        queue=[(k,0)]
        while queue:
            temp=[]
            for node,t in queue:
                if node not in visit:
                    visit[node]=t
                    for nx in graph[node]:
                        temp.append((nx,t+graph[node][nx]))
                elif t<visit[node]:
                    visit[node]=t
                    for nx in graph[node]:
                        temp.append((nx,t+graph[node][nx]))
            queue=temp
        if len(visit)!=n:
            return -1
        return sorted(visit.values())[-1]