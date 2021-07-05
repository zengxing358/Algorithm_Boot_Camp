class Solution:
    def reverseWords(self, s: str) -> str:
        res=[]
        L=len(s)
        i=0
        while i<L:
            while i<L and s[i]==" ":
                i+=1
            j=i
            while i<L and s[i]!=" ":
                i+=1
            if i!=j:
                res.append(s[j:i])
        return ' '.join(res[::-1])
