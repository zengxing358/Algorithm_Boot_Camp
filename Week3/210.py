class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        n=len(prerequisites)
        if n==0:
            return list(range(numCourses))
        degree=[0]*numCourses
        graph=[set() for _ in range(numCourses)]
        for node,need in prerequisites:
            degree[node]+=1
            graph[need].add(node)
        res=[]
        queue=[]
        for i in range(numCourses):
            if degree[i]==0:
                queue.append(i)
        while queue:
            cur=queue.pop(0)
            res.append(cur)
            for neib in graph[cur]:
                degree[neib]-=1
                if degree[neib]==0:
                    queue.append(neib)
        if len(res)==numCourses:
            return res
        return []