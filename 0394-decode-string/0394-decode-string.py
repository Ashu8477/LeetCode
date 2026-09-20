class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        curr=''
        num=0
        for ch in s:
            if ch=='[':
                stack.append((curr,num))
                curr=''
                num=0
            elif ch==']':
                prev,num=stack.pop()
                curr=prev+curr*num
                num=0
            elif ch.isdigit():
                num=num*10 + int(ch)
            else:
                curr+=ch
        return curr

            
        