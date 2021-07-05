class Solution:
    def rob(self, nums: List[int]) -> int:
        l=len(nums)
        self.dic={}
        if l==0:
            return 0
        elif l==1:
            return nums[0]
        elif l==2:
            return max(nums)
        else:
            return max(nums[0]+self._rob(nums[2:-1]),self._rob(nums[1:]))
    def _rob(self,nums):
        l=len(nums)
        if l==0:
            return 0
        elif l==1:
            self.dic[tuple(nums)]=1
            return nums[0]
        elif l==2:
            self.dic[tuple(nums)]=max(nums)
            return self.dic[tuple(nums)]
        elif tuple(nums) in self.dic:
            return self.dic[tuple(nums)]
        else:
            self.dic[tuple(nums)]=max(nums[0]+self._rob(nums[2:]),self._rob(nums[1:]))
            return self.dic[tuple(nums)]
