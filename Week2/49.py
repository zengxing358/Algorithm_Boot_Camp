class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for s in strs:
            hashs=self.gethash(s)
            dic[hashs]=dic.get(hashs,[])+[s]
        return list(dic.values())

    def gethash(self,s):
        res=0
        for i in s:
            res+=10**(ord(i)-ord("a"))
        return res