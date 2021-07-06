class Solution:
    def reverseWords(self, s: str) -> str:
        res=""
        n=len(s)
        i=0
        while i<n:
            start=i
            while i<n and s[i]!=" ":
                i+=1
            for j in range(start,i):
                res+=s[i-1-j+start]
            while i<n and s[i]==" ":
                res+=" "
                i+=1
        return res