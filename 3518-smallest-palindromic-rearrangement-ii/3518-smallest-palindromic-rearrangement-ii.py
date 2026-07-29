from collections import Counter
from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        cnt = Counter(s)

        mid = ""
        freq = [0] * 26

        for ch, c in cnt.items():
            if c & 1:
                mid = ch
            freq[ord(ch) - ord('a')] = c // 2

        m = sum(freq)

        # total distinct permutations of left half
        perm = 1
        rem = m
        for f in freq:
            if f:
                perm *= comb(rem, f)
                rem -= f

        if perm < k:
            return ""

        left = []

        for pos in range(m):
            rem = m - pos

            for i in range(26):
                if freq[i] == 0:
                    continue

                # permutations if current char is fixed here
                nxt = perm * freq[i] // rem

                if k <= nxt:
                    left.append(chr(i + ord('a')))
                    perm = nxt
                    freq[i] -= 1
                    break
                else:
                    k -= nxt

        left = "".join(left)
        return left + mid + left[::-1]