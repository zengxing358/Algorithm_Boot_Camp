class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]

    def push(self, x: int) -> None:
        if self.stack:
            self.stack.append([x,min(self.stack[-1][1],x)])
        else:
            self.stack.append([x,x])

    def pop(self) -> None:
        self.stack.pop()


    def top(self) -> int:
        val,s=self.stack[-1]
        return val

    def getMin(self) -> int:
        val,s=self.stack[-1]
        return s



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()