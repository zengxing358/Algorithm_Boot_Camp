class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(p)<=0:
            return not len(s)
        match=False
        if (len(s)>0)and(p[0]==s[0] or p[0]=='.'):
            match=True
        if len(p)>1 and p[1]=='*':
            return self.isMatch(s,p[2:]) or (match and self.isMatch(s[1:],p))
        else:
            return match and self.isMatch(s[1:],p[1:])