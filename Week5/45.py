class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        maxStep=0
        end=0
        step=0
        for i in range(n-1):
            if maxStep>=i:
                maxStep=max(maxStep,i+nums[i])
                if i==end:
                    end=maxStep
                    step+=1
        return step