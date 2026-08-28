class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        from collections import Counter

        n = len(s)
        cnt = Counter(s)

        if sum(v % 2 for v in cnt.values()) > 1:
            return ""

        half = n // 2
        half_cnt = {c: cnt[c] // 2 for c in cnt}
        chars = sorted(half_cnt)
        center = next((c for c in chars if cnt[c] % 2), "")

        pref = []
        used = Counter()

        for i in range(half):
            c = target[i]
            if used[c] < half_cnt.get(c, 0):
                pref.append(c)
                used[c] += 1
            else:
                break

        rem = half_cnt.copy()
        for c in pref:
            rem[c] -= 1

        def build(p, c, remaining):
            remaining = remaining.copy()
            remaining[c] -= 1
            h = ''.join(pref[:p]) + c
            h += ''.join(x * remaining[x] for x in chars)
            return h + center + h[::-1]

        if len(pref) == half:
            h = ''.join(pref)
            ans = h + center + h[::-1]
            if ans > target:
                return ans

        start = min(len(pref), half - 1)

        for p in range(start, -1, -1):
            if p < len(pref):
                rem[pref[p]] += 1

            for c in chars:
                if c > target[p] and rem[c] > 0:
                    return build(p, c, rem)

        return ""