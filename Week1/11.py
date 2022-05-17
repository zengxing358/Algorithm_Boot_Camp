class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right,result=0,len(height)-1,0
        while left<right:
            if height[left]<height[right]:
                result=max(result,height[left]*(right-left))
                left+=1
            else:
                result=max(result,height[right]*(right-left))
                right-=1
        return result