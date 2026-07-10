class Solution:
    def pathExistenceQueries(
        self,
        n: int,
        nums: List[int],
        maxDiff: int,
        queries: List[List[int]]
    ) -> List[int]:

        order = sorted(range(n), key=lambda i: nums[i])

        pos = [0] * n
        arr = [0] * n

        for i, idx in enumerate(order):
            pos[idx] = i
            arr[i] = nums[idx]

        # next[i] = farthest node reachable in one step
        nxt = [0] * n

        r = 0
        for l in range(n):
            while r + 1 < n and arr[r + 1] - arr[l] <= maxDiff:
                r += 1
            nxt[l] = r

        LOG = 17

        up = [[0] * n for _ in range(LOG)]

        for i in range(n):
            up[0][i] = nxt[i]

        for k in range(1, LOG):
            for i in range(n):
                up[k][i] = up[k - 1][up[k - 1][i]]

        ans = []

        for u, v in queries:

            x = pos[u]
            y = pos[v]

            if x > y:
                x, y = y, x

            if x == y:
                ans.append(0)
                continue

            steps = 0

            for k in range(LOG - 1, -1, -1):
                if up[k][x] < y:
                    x = up[k][x]
                    steps += (1 << k)

            if nxt[x] >= y:
                ans.append(steps + 1)
            else:
                ans.append(-1)

        return ans