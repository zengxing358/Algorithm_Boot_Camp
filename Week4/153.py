class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0]<nums[-1]:
            return nums[0]
        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right)>>1
            if nums[mid]>nums[right]:
                left=mid+1
            else:
                right=mid
        return nums[left]