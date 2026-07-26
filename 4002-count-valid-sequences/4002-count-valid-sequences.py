class Solution:
    def countValidSequences(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        if n < k:
            return 0

        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD

        invfact = [1] * (n + 1)
        invfact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n, 0, -1):
            invfact[i - 1] = invfact[i] * i % MOD

        def C(a, b):
            if b < 0 or b > a:
                return 0
            return fact[a] * invfact[b] % MOD * invfact[a - b] % MOD

        total = C(n - 1, k - 1)

        odd = 0
        if (n - k) % 2 == 0:
            odd = C((n + k - 2) // 2, k - 1)

        return (total - odd) % MOD