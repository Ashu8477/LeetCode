class Solution:
    def minimumPushes(self, word: str) -> int:

        ans = 0
        n = len(word)

        for i in range(n):
            cost = (i // 8) + 1
            ans = ans + cost
        return ans