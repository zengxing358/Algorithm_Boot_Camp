class Solution:
    def validPalindrome(self, s: str) -> bool:
        return self.vaild(s,False)

    def vaild(self,s,frag):
        if len(s)<=1:
            return True
        if s[0]==s[-1]:
                return self.vaild(s[1:-1],frag)
        elif frag:
            return False
        else:
            return self.vaild(s[1:],True) or self.vaild(s[:-1],True)
