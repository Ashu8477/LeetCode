from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:

        n = len(s)
        total_ones = s.count('1')

        zero_len = []
        block_left = []
        block_right = []

        i = 0
        while i < n:
            if s[i] == '0':
                j = i
                while j < n and s[j] == '0':
                    j += 1

                zero_len.append(j - i)
                block_left.append(i)
                block_right.append(j - 1)

                i = j
            else:
                i += 1

        m = len(zero_len)

        if m < 2:
            return [total_ones] * len(queries)

        tmp = [zero_len[i] + zero_len[i + 1] for i in range(m - 1)]

        lg = [0] * (len(tmp) + 1)
        for i in range(2, len(tmp) + 1):
            lg[i] = lg[i // 2] + 1

        st = [tmp]

        k = 1
        while (1 << k) <= len(tmp):
            prev = st[-1]

            cur = [
                max(prev[i], prev[i + (1 << (k - 1))])
                for i in range(len(tmp) - (1 << k) + 1)
            ]

            st.append(cur)
            k += 1

        def query_max(l: int, r: int) -> int:
            if l > r:
                return 0

            p = lg[r - l + 1]

            return max(
                st[p][l],
                st[p][r - (1 << p) + 1]
            )

        ans = []

        for l, r in queries:

            i = bisect_left(block_right, l)
            j = bisect_right(block_left, r) - 1

            if i >= m or j < 0 or i >= j:
                ans.append(total_ones)
                continue

            first_len = block_right[i] - max(block_left[i], l) + 1
            last_len = min(block_right[j], r) - block_left[j] + 1

            if j == i + 1:
                best_gain = first_len + last_len
            else:
                val1 = first_len + zero_len[i + 1]
                val2 = zero_len[j - 1] + last_len
                val3 = query_max(i + 1, j - 2)

                best_gain = max(val1, val2, val3)

            ans.append(total_ones + best_gain)

        return ans