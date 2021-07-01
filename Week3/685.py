"""
https://leetcode-cn.com/problems/redundant-connection-ii/
并查集解法
"""
class Solution:
    def findRedundantDirectedConnection(self, edges):
        self.lst={i:i for i in range(1,len(edges)+1)}
        self.size={i:i for i in range(1,len(edges)+1)}
        father={}
        res=[]
        t=[]
        for u,v in edges:
            if v not in father:
                father[v]=u
                if not self.connect(u,v):
                    t.extend([u,v])
            else:
                res.extend([u,v])
        if not res:
            return t
        if self.isallconnect():
            return res
        return [father[res[1]],res[1]]
    def getparent(self,node):
        if node!=self.lst[node]:
            return self.getparent(self.lst[node])
        return node
    def isallconnect(self):
        temp=0
        for key,value in self.lst.items():
            if key==value:
                temp+=1
        return temp==1
    def connect(self,u,v):
        uparent=self.getparent(u)
        vparent=self.getparent(v)
        if uparent==vparent:
            return False
        usize=self.size[uparent]
        vsize=self.size[vparent]
        if usize>=vsize:
            self.lst[vparent]=uparent
            if usize==vsize:
                self.size[uparent]+=1
        else:
            self.lst[uparent]=vparent
        return True