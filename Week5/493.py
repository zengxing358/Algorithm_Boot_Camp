class Solution:
    def reversePairs(self, nums):
        self.res=0
        self.mergesort(nums)
        return self.res
    def mergesort(self,nums):
        n=len(nums)
        if n<=1:
            return nums
        mid=n//2
        left=self.mergesort(nums[:mid])
        right=self.mergesort(nums[mid:])
        res=[]
        m=len(left)
        n=len(right)
        i,j=0,0
        while i<m and j<n:
            if left[i]>2*right[j]:
                self.res+=m-i
                j+=1
            else:
                i+=1
        i,j=0,0
        while i<m and j<n:
            if left[i]<=right[j]:
                res.append(left[i])
                i+=1
            else:
                res.append(right[j])
                j+=1
        if i<m:
            res+=left[i:]
        if j<n:
            res+=right[j:]
        return res