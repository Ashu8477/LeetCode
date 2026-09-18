class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = i

        intervals = []

        for i in range(n):
            idx = ord(s[i]) - ord('a')

            if first[idx] != i:
                continue

            end = last[idx]
            j = i
            valid = True

            while j <= end:
                curr = ord(s[j]) - ord('a')

                if first[curr] < i:
                    valid = False
                    break

                end = max(end, last[curr])
                j += 1

            if valid:
                intervals.append((i, end))

        intervals.sort(key=lambda x: x[1])

        ans = []
        prev_end = -1

        for start, end in intervals:
            if start > prev_end:
                ans.append(s[start:end + 1])
                prev_end = end

        return ans