class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        self.bloomDay=bloomDay
        self.m=m
        self.k=k
        if m*k>len(bloomDay):
            return -1
        temp=list(set(bloomDay))
        temp.sort()
        left=0
        right=len(temp)-1
        while left<right:
            mid=(left+right)//2
            if self.Mday(temp[mid]):
                right=mid
            else:
                left=mid+1
        return temp[left]
    def Mday(self,index):
        last=-1
        count=self.m
        for cur in range(len(self.bloomDay)):
            if self.bloomDay[cur]>index:
                last=cur
            else:
                if cur-last==self.k:
                    count-=1
                    last=cur
        return count<=0