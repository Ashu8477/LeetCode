class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:

        n = len(arr)
        INF = float("inf")

        dp = [INF] * (n + 1)

        left = 0
        curr_sum = 0
        ans = INF

        for right in range(n):

            curr_sum += arr[right]

            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            if curr_sum == target:

                length = right - left + 1

                if dp[left] != INF:
                    ans = min(ans, length + dp[left])

                dp[right + 1] = min(dp[right], length)

            else:
                dp[right + 1] = dp[right]

        return -1 if ans == INF else ans