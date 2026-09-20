class MinStack:

    def __init__(self):
        self.stack=[]
        self.ministack=[]
        

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.ministack:
            self.ministack.append(value)
        else:
            self.ministack.append(min(value,self.ministack[-1]))
        

    def pop(self) -> None:
        self.stack.pop()
        self.ministack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.ministack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()