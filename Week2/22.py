from functools import lru_cache
class Solution:
    @lru_cache(None)
    def generateParenthesis(self, n: int) -> List[str]:
        if n==1:
            return ["()"]
        else:
            res=set()
            temp=self.generateParenthesis(n-1)
            for s in temp:
                for i in range(len(s)):
                    ss=s[:i]+'()'+s[i:]
                    res.add(ss)
            return list(res)