class NumArray:
    
    def __init__(self, nums: List[int]):
        self.n=len(nums)
        self.tree=[0 for _ in range(self.n+1)]
        for i in range(1,self.n+1):
            self.tree[i]=sum(nums[i-self.getkbit(i):i])

    def getkbit(self,k):
        return k&-k

    def update(self, index: int, val: int) -> None:
        diff=val-self.sumRange(index,index)
        n=index+1
        while n<=self.n:
            self.tree[n]+=diff
            n+=self.getkbit(n)

    def sumRange(self, left: int, right: int) -> int:
        if left==0:
            return self.getprefix(right+1)
        return self.getprefix(right+1)-self.getprefix(left)

    def getprefix(self,n):
        res=0
        while n:
            res+=self.tree[n]
            n-=self.getkbit(n)
        return res