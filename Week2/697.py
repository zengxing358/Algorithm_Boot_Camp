class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dic1={}
        dic2={}
        for index,val in enumerate(nums):
            dic1[val]=dic1.get(val,0)+1
            dic2[val]=dic2.get(val,[])+[index]
        v=sorted(dic1,key=dic1.get,reverse=True)
        res=len(nums)
        i=0
        cur=dic1[v[i]]
        while i<len(v) and dic1[v[i]]==cur:
            res=min(dic2[v[i]][-1]-dic2[v[i]][0]+1,res)
            i+=1
        return res