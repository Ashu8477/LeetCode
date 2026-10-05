class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        stack = []
        score = 0

        for ch in s:

            if ch == '(':
                stack.append(score)
                score = 0

            else:
                if score == 0:
                    score = 1
                else:
                    score = 2 * score

                score += stack.pop()

        return score