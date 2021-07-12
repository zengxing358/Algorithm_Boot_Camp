class Solution:
    def countRangeSum(self, nums, lower: int, upper: int) -> int:
        self.lower=lower
        self.upper=upper
        self.res=0
        n=len(nums)
        pre=[0]*(n+1)
        for i in range(n):
            pre[i+1]=pre[i]+nums[i]
        self.mergesort(pre)
        return self.res
    def mergesort(self,nums):
        n=len(nums)
        if n<=1:
            return nums
        mid=n//2
        leftnums=self.mergesort(nums[:mid])
        rightnums=self.mergesort(nums[mid:])
        leftlen=len(leftnums)
        rightlen=len(rightnums)
        i=0
        j1,j2=0,0
        while i<leftlen:
            while j1<rightlen and rightnums[j1]-leftnums[i]<self.lower:
                j1+=1
            while j2<rightlen and rightnums[j2]-leftnums[i]<=self.upper:
                j2+=1
            self.res+=j2-j1
            i+=1
        i,j=0,0
        res=[]
        while i<leftlen and j<rightlen:
            if leftnums[i]<=rightnums[j]:
                res.append(leftnums[i])
                i+=1
            else:
                res.append(rightnums[j])
                j+=1
        if i<leftlen:
            res+=leftnums[i:]
        if j<rightlen:
            res+=rightnums[j:]
        return res