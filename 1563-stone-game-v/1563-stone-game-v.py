class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        prefix = [0] * (n + 1)

        for i, x in enumerate(stoneValue):
            prefix[i + 1] = prefix[i] + x

        dp = [[0] * n for _ in range(n)]
        maxL = [[0] * n for _ in range(n)]
        maxR = [[0] * n for _ in range(n)]

        for i in range(n):
            maxL[i][i] = stoneValue[i]
            maxR[i][i] = stoneValue[i]

        for l in range(n - 1, -1, -1):
            p = l - 1

            for r in range(l + 1, n):

                while p + 1 < r:
                    left = prefix[p + 2] - prefix[l]
                    right = prefix[r + 1] - prefix[p + 2]

                    if left <= right:
                        p += 1
                    else:
                        break

                if p >= l:
                    dp[l][r] = max(
                        dp[l][r],
                        maxL[l][p]
                    )

                if p + 2 <= r:
                    dp[l][r] = max(
                        dp[l][r],
                        maxR[p + 2][r]
                    )

                if p >= l:
                    left = prefix[p + 1] - prefix[l]
                    right = prefix[r + 1] - prefix[p + 1]

                    if left == right:
                        dp[l][r] = max(
                            dp[l][r],
                            maxR[p + 1][r]
                        )

                total = prefix[r + 1] - prefix[l]

                maxL[l][r] = max(
                    maxL[l][r - 1],
                    dp[l][r] + total
                )

                maxR[l][r] = max(
                    maxR[l + 1][r],
                    dp[l][r] + total
                )

        return dp[0][n - 1]