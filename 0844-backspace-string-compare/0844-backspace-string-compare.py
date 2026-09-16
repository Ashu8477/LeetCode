class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i=len(s)-1
        j=len(t)-1
        skipS=skipT=0
        while i>=0 or j>=0:
            while i>=0:
                if s[i]=='#':
                    skipS+=1
                    i-=1
                elif skipS:
                    skipS-=1
                    i-=1
                else:
                    break
            while j>=0:
                if t[j]=='#':
                    skipT+=1
                    j-=1
                elif skipT:
                    skipT-=1
                    j-=1
                else:
                    break
            if s[i]!=t[j] and i>=0 and j>=0:
                return False
            
            if (i>=0) != (j>=0):
                return False
            
            i-=1
            j-=1
        return True

        