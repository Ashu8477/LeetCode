class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        ans=[]
        col=set()
        d1=set()
        d2=set()
        board=[['.']*n for _ in range(n)]


        def solve(r):

            if r==n:
                ans.append([''.join(row) for row in board])
                return
            
            for c in range(n):
                if c in col or (r-c) in d1 or (r+c) in d2:
                    continue

                board[r][c]='Q'
                col.add(c)
                d1.add(r-c)
                d2.add(r+c)

                solve(r+1)

                board[r][c]='.'
                col.remove(c)
                d1.remove(r-c)
                d2.remove(r+c)
        solve(0)
        return ans

