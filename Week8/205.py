class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dic1={}
        dic2={}
        for i in range(len(s)):
            a,b=s[i],t[i]
            if a in dic1 and b!=dic1[a]:
                return False
            if b in dic2 and a!=dic2[b]:
                return False
            dic1[a]=b
            dic2[b]=a
        return True
