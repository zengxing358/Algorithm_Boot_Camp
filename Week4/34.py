class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res=[-1,-1]
        l=len(nums)
        for i in range(l):
            if nums[i]>target:
                if res[0]!=-1:
                    res[1]=i-1
                break
            if nums[i]== target:
                if res[0]==-1:
                    res[0]=i
        else:
            if res[0]!=-1:
                res[1]=l-1
        return res
            