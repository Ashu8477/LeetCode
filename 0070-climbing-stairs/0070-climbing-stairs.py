class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp=[0]*(n+1)
        dp[1]=1
        dp[2]=2

        def solve(n):
            if dp[n]!=0:
                return dp[n]
            dp[n]=solve(n-1)+solve(n-2)
            return dp[n]
        return solve(n)

        