class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        prev=0
        for ch in operations:
            
            if ch=='C':
                stack.pop()
            elif ch=='D':
                stack.append(2*stack[-1])
            elif ch=='+':
                
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(ch))
        return sum(stack)


        