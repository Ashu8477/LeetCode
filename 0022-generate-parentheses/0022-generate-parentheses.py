class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(s, open_c, close_c):
            if len(s) == 2 * n:
                res.append(s)
                return
            
            if open_c < n:
                backtrack(s + "(", open_c + 1, close_c)
            
            if close_c < open_c:
                backtrack(s + ")", open_c, close_c + 1)

        backtrack("", 0, 0)
        return res