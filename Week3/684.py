"""
https://leetcode-cn.com/problems/redundant-connection/
并查集解法
"""
class Solution:
    def findRedundantConnection(self, edges):
        self.lst={i:i for i in range(1,len(edges)+1)}
        self.size={i:0 for i in range(1,len(edges)+1)}
        for u,v in edges:
            con=self.connect(u,v)
            if not con:
                if u>v:
                    return [v,u]
                else:
                    return [u,v]
    def getparent(self,node):
        if node!=self.lst[node]:
            return self.getparent(self.lst[node])
        return node
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