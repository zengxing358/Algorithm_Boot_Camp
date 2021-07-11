import heapq
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        heap=[]
        pre=0
        lst=[[building[0],-building[2],building[1]] for building in buildings]+[[building[1],0,0] for building in buildings]
        lst.sort()
        res=[]
        for cur,height,right in lst:
            if height:
                heapq.heappush(heap,(height,right))
            else:
                while heap:
                    if heap[0][1]<=cur:
                        heapq.heappop(heap)
                    else:
                        break
            if heap and heap[0][0]!=-pre:
                pre=-heap[0][0]
                res.append([cur,pre])
            elif not heap and pre!=0:
                pre=0
                res.append([cur,pre])
        return res