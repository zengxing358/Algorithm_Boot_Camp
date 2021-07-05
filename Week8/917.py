class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        lst=list(S)
        res=''
        for s in S:
            if s.isalpha():
                while True:
                    tmp=lst.pop()
                    if tmp.isalpha():
                        res+=tmp
                        break
            else:
                res+=s
        return res
