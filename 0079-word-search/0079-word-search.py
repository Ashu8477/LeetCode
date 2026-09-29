class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:

        row=len(board)
        col=len(board[0])

        def dfs(r,c,idx):
            if idx==len(word):
                return True
            
            if r<0 or c<0 or r>=row or c>=col:
                return False

            if board[r][c]!=word[idx]:
                return False
            
            temp=board[r][c]
            board[r][c]='#'
            found=(
                dfs(r+1,c,idx+1) or
                dfs(r-1,c,idx+1) or
                dfs(r,c+1,idx+1) or
                dfs(r,c-1,idx+1)
            )
            board[r][c]=temp
            return found

        for r in range(row):
            for c in range(col):
                if dfs(r,c,0):
                    return True
        return False

        