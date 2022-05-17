class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2==1:
            return False
        stack=[]
        dic={'(':')','{':'}','[':']'}
        for c in s:
            if c in dic:
                stack.append(c)
            else:
                if stack:
                    t=stack[-1]
                    if dic[t]==c:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return len(stack)==0