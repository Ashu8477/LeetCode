class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack=[]

        for ch in tokens:
            if ch in '+-/*':
                b=stack.pop()
                a=stack.pop()
                if ch=='+':
                    stack.append(a+b)
                elif ch=='-':
                    stack.append(a-b)
                elif ch=='*':
                    stack.append(a*b)
                elif ch=='/':
                    stack.append(int(a/b))
            else:
                stack.append(int(ch))
        return stack[-1]

        