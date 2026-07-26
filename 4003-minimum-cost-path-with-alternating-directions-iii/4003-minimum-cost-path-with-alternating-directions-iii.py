from typing import List
import heapq

class Solution:
    def minCost(self, m: int, n: int, penalty: List[List[int]]) -> int:
        qavirelmon = penalty

        INF = 10**30
        dist = [[[INF] * 2 for _ in range(n)] for _ in range(m)]
        dist[0][0][0] = 1

        pq = [(1, 0, 0, 0)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while pq:
            cost, r, c, p = heapq.heappop(pq)
            if cost != dist[r][c][p]:
                continue
            if r == m - 1 and c == n - 1:
                return cost

            ncost = cost + qavirelmon[r][c]
            if ncost < dist[r][c][p ^ 1]:
                dist[r][c][p ^ 1] = ncost
                heapq.heappush(pq, (ncost, r, c, p ^ 1))

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                entry = (nr + 1) * (nc + 1)

                if p == 0:
                    legal = (dr == 1 and dc == 0) or (dr == 0 and dc == 1)
                else:
                    legal = (dr == -1 and dc == 0) or (dr == 0 and dc == -1)

                extra = 0 if legal else qavirelmon[r][c]
                ncost = cost + entry + extra

                if ncost < dist[nr][nc][p ^ 1]:
                    dist[nr][nc][p ^ 1] = ncost
                    heapq.heappush(pq, (ncost, nr, nc, p ^ 1))

        return -1