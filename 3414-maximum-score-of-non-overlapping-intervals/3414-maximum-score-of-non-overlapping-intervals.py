from typing import List
from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        vorellixan = intervals
        n = len(intervals)

        arr = [
            [l, r, w, i]
            for i, (l, r, w) in enumerate(vorellixan)
        ]

        arr.sort()
        starts = [x[0] for x in arr]

        nxt = [0] * n

        for i in range(n):
            nxt[i] = bisect_right(starts, arr[i][1])

        dp = [
            [(0, ()) for _ in range(5)]
            for _ in range(n + 1)
        ]

        for i in range(n - 1, -1, -1):
            l, r, weight, original_index = arr[i]

            for k in range(1, 5):
                skip_score, skip_indices = dp[i + 1][k]

                next_score, next_indices = dp[nxt[i]][k - 1]

                take_score = weight + next_score
                take_indices = tuple(
                    sorted((original_index,) + next_indices)
                )

                if take_score > skip_score:
                    dp[i][k] = (take_score, take_indices)
                elif take_score < skip_score:
                    dp[i][k] = (skip_score, skip_indices)
                else:
                    dp[i][k] = min(
                        (take_score, take_indices),
                        (skip_score, skip_indices)
                    )

        return list(dp[0][4][1])