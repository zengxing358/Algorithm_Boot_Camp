class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        n=len(nums)
        for i in range(n-2):
            if i>0 and nums[i-1]==nums[i]:
                continue
            if k:=self.twosum(nums,i+1,n,-nums[i]):
                res.extend([[nums[i]]+j for j in k])
        return res
    def twosum(self,nums,start,end,target):
        res=[]
        right=end-1
        for i in range(start,end-1):
            if i>start and nums[i]==nums[i-1]:
                continue
            while i<right and nums[i]+nums[right]>target:
                right-=1
            if i<right and nums[i]+nums[right]==target:
                res.append([nums[i],nums[right]])
        return res