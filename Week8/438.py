class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        np=list(p)
        np.sort()
        l=len(np)
        L=len(s)
        ns=list(s)
        res=[]
        for i in range(L-l+1):
            ins=ns[i:i+l]
            ins.sort()
            if ins==np:
                res.append(i)
        return res