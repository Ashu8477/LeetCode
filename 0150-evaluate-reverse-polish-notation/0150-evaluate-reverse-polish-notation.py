class Solution:
    def evalRPN(self, tokens: list[str]) -> int:

        stack=[]
        value=0
        if len(tokens)==1:
            return int(tokens[0])
        for token in tokens:
            if token=='+':
                value=stack[-2]+stack[-1]
                stack.pop()
                stack.pop()
                stack.append(value)
            elif token=='*':
                value=stack[-2]*stack[-1]
                stack.pop()
                stack.pop()
                stack.append(value)
            elif token=='/':
                value=int(stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(value)
            elif token=='-':
                value=stack[-2]-stack[-1]
                stack.pop()
                stack.pop()
                stack.append(value)
            else:
                stack.append(int(token))
        return stack[-1]