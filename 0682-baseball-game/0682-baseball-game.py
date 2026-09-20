class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack=[]

        for ch in operations:
            if ch.lstrip('-').isdigit():
                stack.append(int(ch))
            elif ch=='C':
                stack.pop()
            elif ch=='D':
                stack.append(2*stack[-1])
            elif ch=='+':
                stack.append(stack[-1]+stack[-2])
        return sum(stack) 