class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quick(N):
            cur=x
            res=1
            s=bin(N)[2:][::-1]
            for i in s:
                if i=="1":
                    res*=cur
                cur*=cur
            return res
        return quick(n) if n>0 else 1.0/quick(n*-1)