
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n=len(nums)
        arr=[0]*(n+1)
        dic={0:1}
        res=0
        for i in range(n):
            arr[i+1]=arr[i]+nums[i]%2
            if arr[i+1]-k>=0:
                res+=dic[arr[i+1]-k]
            dic[arr[i+1]]=dic.get(arr[i+1],0)+1
        return res