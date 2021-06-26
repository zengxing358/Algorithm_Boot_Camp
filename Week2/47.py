class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        L=len(nums)
        if L==1:
            return [nums]
        res=set()
        first=self.permuteUnique(nums[1:])
        for item in first:
            for i in range(L):
                temp=item[:i]+[nums[0]]+item[i:]
                res.add(tuple(temp))
        return [list(s) for s in res]
