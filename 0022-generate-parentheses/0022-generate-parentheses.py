class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans=[]
        path=[]

        def solve(open,close):
            if n==open and n==close:
                ans.append("".join(path))
                return
            
            if open<n:
                path.append('(')
                solve(open+1,close)
                path.pop()
            
            if close<open:
                path.append(')')
                solve(open,close+1)
                path.pop()
        solve(0,0)
        return ans