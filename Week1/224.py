class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        l=len(s)
        i=0
        sign=True
        dic={"+":True,"-":False}
        while i<l:
            if s[i]=="(":
                stack.append(s[i])
            elif s[i].isdigit():
                temp=s[i]
                while i+1<l and s[i+1].isdigit():
                    i+=1
                    temp+=s[i]
                if sign:
                    stack.append(int(temp))
                else:
                    stack.append(int(temp)*-1)
                    sign=True
            elif s[i]==")":
                temp=[]
                while stack[-1]!="(":
                    temp.append(stack.pop())
                first=temp.pop()
                while temp:
                    op=temp.pop()
                    sencond=temp.pop()
                    if op=="+":
                        first=first+sencond
                    else:
                        first=first-sencond
                stack[-1]=first
            elif s[i]=="+" or s[i]=="-":
                if stack and type(stack[-1])==str:
                    sign=dic[s[i]]
                else:
                    stack.append(s[i])
            i+=1
        if type(stack[0])==str:
            if dic[stack[0]]:
                first=stack[1]
            else:
                first=stack[1]*-1
            stack=stack[2:]
        else:
            first=stack[0]
            stack=stack[1:]
        for i in range(0,len(stack),2):
            if stack[i]=="+":
                first=first+stack[i+1]
            else:
                first=first-stack[i+1]
        return first