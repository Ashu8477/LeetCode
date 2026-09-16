class MinStack:

    def __init__(self):
        self.stack=[]
        self.miniStack=[]
    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.miniStack:
            self.miniStack.append(value)
        else:
            self.miniStack.append(min(value,self.miniStack[-1]))
        
    def pop(self) -> None:
        
        self.stack.pop()
        
        self.miniStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        
        return self.miniStack[-1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()