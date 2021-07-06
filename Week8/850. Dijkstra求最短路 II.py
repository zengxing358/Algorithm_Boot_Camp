first=input()
n,m=[int(i) for i in first.split()]
import collections, heapq
graph=collections.defaultdict(list)
for i in range(m):
    temp=input()
    a, b, c=[int(j) for j in temp.split()]
    graph[a].append([c,b])
visit=set()
queue=[]
heapq.heappush(queue,[0,1])
distance=[float("inf")]*(n+1)
distance[1]=0
while queue:
    dis,v=heapq.heappop(queue)
    if v not in visit:
        visit.add(v)
        for d,j in graph[v]:
            if distance[j]>d+distance[v]:
                distance[j]=d+distance[v]
                heapq.heappush(queue,[distance[j],j])
print(distance[n] if distance[n] != float("inf") else -1)