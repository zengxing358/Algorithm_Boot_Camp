class Solution:
    def firstUniqChar(self, s: str) -> int:
        s1=set()
        s2=set()
        for i in s:
            if i in s1:
                s2.add(i)
            s1.add(i)
        for index,i in enumerate(s):
            if i in s1-s2:
                return index
        return -1