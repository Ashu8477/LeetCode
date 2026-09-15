class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i - 1]

            # length k palindrome
            if i >= k and s[i - k:i] == s[i - k:i][::-1]:
                dp[i] = max(dp[i], dp[i - k] + 1)

            # length k+1 palindrome
            if i >= k + 1 and s[i - k - 1:i] == s[i - k - 1:i][::-1]:
                dp[i] = max(dp[i], dp[i - k - 1] + 1)

        return dp[n]