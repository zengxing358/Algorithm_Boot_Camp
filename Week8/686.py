import math
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if b:
            n=len(b)
            cnt=math.ceil(n/len(a))
            if b in a*cnt:
                return cnt
            if b in a*(cnt+1):
                return cnt+1
            return -1
        return 0