import heapq
class Solution:
    def minInterval(self, intervals, queries):
        intervals.sort()
        QL=len(queries)
        res=[-1]*QL
        q=sorted([(i,v) for i,v in enumerate(queries)],key=lambda x:x[1])
        j=0
        inter=len(intervals)
        heap=[]
        for i,x in q:
            while j<inter and intervals[j][0]<=x:
                left,right=intervals[j]
                heapq.heappush(heap,(right-left+1,right))
                j+=1
            while heap and heap[0][1]<x:
                heapq.heappop(heap)
            if heap:
                res[i]=heap[0][0]
        return res