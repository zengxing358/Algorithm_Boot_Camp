class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.dic={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        self.l=len(digits)
        if self.l<1:
            return []
        elif self.l==1:
            return list(self.dic[digits])
        else:
            self.digits=digits
            return self._comb(0)
    def _comb(self,cur):
        if cur==self.l-1:
            return list(self.dic[self.digits[cur]])
        else:
            return [i+j for i in list(self.dic[self.digits[cur]]) for j in self._comb(cur+1)]