class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(len(tokens)):
            if tokens[i]=="+":
                stack.append(int(stack.pop()+stack.pop()))
            elif tokens[i]=="-":
                s=stack.pop()
                f=stack.pop()
                stack.append(int(f-s))
            elif tokens[i]=="*":
                stack.append(int(stack.pop()*stack.pop()))
            elif tokens[i]=="/":
                s=stack.pop()
                f=stack.pop()
                stack.append(int(f/s))
            else:
                stack.append(int(tokens[i]))
        return stack[-1]