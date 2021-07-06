class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        cur=1
        while n>cur:
            if n&cur==cur:
                return False
            cur=cur<<1
        return n==cur