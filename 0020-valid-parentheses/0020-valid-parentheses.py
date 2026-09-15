class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mp={')':'(','}':'{',']':'['}

        for ch in s:
            if ch in mp:
                if not stack or stack[-1]!=mp[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack


        