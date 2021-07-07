import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums,0,len(nums))
        return nums
    def quicksort(self,nums,start,end):
        if start+1>=end:
            return
        n=random.randint(start,end-1)
        nums[start],nums[n]=nums[n],nums[start]
        left=start+1
        right=end
        while left<right:
            if nums[left]<=nums[start]:
                left+=1
            else:
                right-=1
                nums[left],nums[right]=nums[right],nums[left]
        nums[start],nums[left-1]=nums[left-1],nums[start]
        self.quicksort(nums,start,left-1)
        self.quicksort(nums,left,end)