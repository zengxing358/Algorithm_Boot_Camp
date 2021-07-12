class Tree:
    def __init__(self,n):
        self.tree=[0]*(n+1)
        self.n=n

    def lowbit(self,x):
        return x&-x

    def query(self,x):
        res = 0
        while x > 0:
            res += self.tree[x]
            x -= self.lowbit(x)
        return res

    def update(self,x):
        while x <= self.n:
            self.tree[x] += 1
            x += self.lowbit(x)

class Solution:
    def countRangeSum(self, nums, lower: int, upper: int) -> int:
        n=len(nums)
        pre=[0]*(n+1)
        for i in range(n):
            pre[i+1]=pre[i]+nums[i]
        s=set()
        for p in pre:
            s.add(p)
            s.add(p-lower)
            s.add(p-upper)
        s=list(s)
        s.sort()
        n2=len(s)
        dic={}
        for key,val in enumerate(s):
            dic[val]=key+1
        res=0
        tree=Tree(n2)
        for p in pre:
            left=dic[p-lower]
            right=dic[p-upper]
            res+=tree.query(left)-tree.query(right-1)
            tree.update(dic[p])
        return res