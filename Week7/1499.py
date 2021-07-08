class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        queue=[]
        res=-float("inf")
        for x,y in points:
            while queue and x-queue[0][0]>k:
                queue=queue[1:]
            if queue:
                res=max(res,x-queue[0][0]+queue[0][1]+y)
            while queue and queue[-1][1]-queue[-1][0]<y-x:
                queue.pop()
            queue.append((x,y))
        return res