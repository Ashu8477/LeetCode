class Solution:
    def aggregateTimeSeries(self, series1: List[List[int]], series2: List[List[int]]) -> List[List[int]]:
        times = sorted({t for t, _ in series1} | {t for t, _ in series2})

        ans = []
        i = j = 0
        n, m = len(series1), len(series2)

        for t in times:
            while i < n and series1[i][0] < t:
                i += 1
            while j < m and series2[j][0] < t:
                j += 1

            v1 = series1[i][1] if i < n else 0
            v2 = series2[j][1] if j < m else 0

            ans.append([t, v1 + v2])

        return ans