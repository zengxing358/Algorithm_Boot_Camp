class Solution:
    def trap(self, height: List[int]) -> int:
        if height:
            n=len(height)
            maxnum=-1
            rightmax=[0]*n
            for i in range(n-1,-1,-1):
                if height[i]>maxnum:
                    maxnum=height[i]
                rightmax[i]=maxnum
            maxnum=height[0]
            ans=0
            for i in range(1,n):
                h=min(maxnum,rightmax[i])
                ans+=max(h-height[i],0)
                maxnum=max(maxnum,height[i])
            return ans    

        return 0

