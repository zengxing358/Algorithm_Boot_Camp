class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k==1:
            return [[i] for i in range(1,n+1)]
        else:
            res=[]
            temp=self.combine(n,k-1)
            for t in temp:
                j=t[-1]+1
                while j<=n:
                    res.append(t+[j])
                    j+=1
            return res