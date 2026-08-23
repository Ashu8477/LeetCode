class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        diff = 0
        q = 0

        for i in range(n):
            if num[i] == '?':
                q += 1 if i < n // 2 else -1
            else:
                diff += int(num[i]) if i < n // 2 else -int(num[i])

        return 2 * diff != -9 * q