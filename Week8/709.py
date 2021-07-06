class Solution:
    def toLowerCase(self, s: str) -> str:
        lst=list(s)
        for i,v in enumerate(lst):
            if lst[i]>="A" and lst[i]<="Z":
                lst[i]=chr(ord(lst[i])-ord("A")+ord("a"))
        return "".join(lst)