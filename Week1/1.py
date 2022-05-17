class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst=[]
        for idx,val in enumerate(nums):
            lst.append((val,idx))
        lst.sort(key=lambda x:x[0])
        left=0
        right=len(lst)-1
        while left<right:
            if lst[left][0]+lst[right][0]==target:
                return [lst[left][1],lst[right][1]]
            elif lst[left][0]+lst[right][0]>target:
                right-=1
            else:
                left+=1