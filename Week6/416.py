class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumnum=sum(nums)
        if sumnum%2==1:
            return False
        else:
            sumn=int(sumnum/2)
            mse=[nums[0]==i for i in range(sumn+1)]
            for i in range(1,len(nums)):
                for j in range(sumn,nums[i]-1,-1):
                    mse[j]=mse[j]|(mse[j-nums[i]])
            return mse[-1]