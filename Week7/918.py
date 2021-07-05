class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        r1=float("inf")
        r2=-float("inf")
        end1=end2=0
        for val in A:
            end1=min(0,end1)+val
            end2=max(0,end2)+val
            r1=min(r1,end1)
            r2=max(r2,end2)
            
        m=max(A)
        return m if m<0 else max(r2,sum(A)-r1)
