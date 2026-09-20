class Solution:
    def isValid(self, s: str) -> bool:
        mp={']':'[','}':'{',')':'('}
        stack=[]
        for ch in s:
            if ch in mp:
                if stack:
                    if stack[-1]==mp[ch]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            else:
                stack.append(ch)
        return not stack
