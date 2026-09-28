class Solution:
    def partition(self, s: str) -> list[list[str]]:

        ans=[]


        def solve(path,start):
            if start==len(s):
                ans.append(path[:])
                return
            
            for end in range(start,len(s)):
                substring=s[start:end+1]
                if substring==substring[::-1]:
                    path.append(substring)
                    solve(path,end+1)
                    path.pop()
        solve([],0)
        return ans
        