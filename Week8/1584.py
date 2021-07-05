class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        self.lst=list(range(n))
        self.size=[0]*n
        weights=[]
        for i in range(n-1):
            for j in range(i+1,n):
                weights.append((i,j,abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])))
        weights.sort(key=lambda x:x[2],reverse=True)
        res=0
        while weights:
            nodeA,nodeB,cost=weights.pop()
            con=self.connect(nodeA,nodeB)
            if con:
                res+=cost
        return res

    def getparent(self,node):
        if node !=self.lst[node]:
            return self.getparent(self.lst[node])
        return node
    def connect(self,p,q):
        pfather=self.getparent(p)
        qfather=self.getparent(q)
        if pfather==qfather:
            return False
        psize=self.size[pfather]
        qsize=self.size[qfather]
        if psize>=qsize:
            self.lst[qfather]=pfather
            if psize==qsize:
                self.size[pfather]+=1
        else:
            self.lst[pfather]=qfather
        return True