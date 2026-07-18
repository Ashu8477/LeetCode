class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])

        def dfs(i, j, k):
            if k == len(word):
                return True
            if i < 0 or i >= n or j < 0 or j >= m or board[i][j] != word[k]:
                return False

            tem = board[i][j]
            board[i][j] = "#"

            found = (
                dfs(i + 1, j, k + 1)
                or dfs(i - 1, j, k + 1)
                or dfs(i, j - 1, k + 1)
                or dfs(i, j + 1, k + 1)
            )
            board[i][j] = tem
            return found

        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0):
                    return True
        return False
