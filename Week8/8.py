class Solution:
    def myAtoi(self, s: str) -> int:
        frag=False
        temp=[]
        i=0
        L=len(s)
        while i<L:
            if s[i]=="-":
                if not frag:
                    f=-1
                    frag=True
                    i+=1
                else:
                    return 0
            elif s[i]=="+":
                if not frag:
                    f=1
                    i+=1
                    frag=True
                else:
                    return 0
            elif s[i].isdigit():
                while i<L and s[i].isdigit():
                    temp.append(s[i])
                    i+=1
                if not frag:
                    f=1
                res=f*int(''.join(temp))
                if res<-2147483648:
                    return -2147483648
                elif res>2147483647:
                    return 2147483647
                return res
            elif s[i]==" ":
                if frag:
                    return 0
                i+=1
            else:
                return 0

        return 0
                