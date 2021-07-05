class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        self.dic={}
        tree=self.dic
        count=0
        for s in strs[0]:
            tree[s]={}
            tree=tree[s]
            count+=1
        for st in strs[1:]:
            temp=0
            tree=self.dic
            for i in range(count):
                if st[i] not in tree:
                    break
                temp+=1
                tree=tree[st[i]]
            if not temp:
                return ""
            count=min(count,temp)
        res=''
        tree=self.dic
        for i in range(count):
            for t in tree:
                res+=t
                tree=tree[t]
        return res