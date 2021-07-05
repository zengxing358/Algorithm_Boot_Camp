class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left=max(nums)
        right=sum(nums)
        L=len(nums)
        while left<right:
            mid=(left+right)//2
            s,cnt=0,1
            for i in range(L):
                if s+nums[i]>mid:
                    s=0
                    cnt+=1
                s+=nums[i]
            if cnt<=m:
                right=mid
            else:
                left=mid+1
                
        return left
