class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        N=len(nums)
        result=[-float(inf)]*(N+1)
        result[0]=0
        result[1]=nums[0]
        for i in range(1,N):
            result[i+1]=max(result[i]+nums[i],nums[i])
        return max(result[1:])