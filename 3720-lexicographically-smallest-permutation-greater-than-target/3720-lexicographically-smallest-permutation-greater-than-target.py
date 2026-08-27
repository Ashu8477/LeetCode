class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        pivot = -1

        for i, ch in enumerate(target):
            x = ord(ch) - ord('a')

            for c in range(x + 1, 26):
                if cnt[c] > 0:
                    pivot = i
                    break

            if cnt[x] == 0:
                break

            cnt[x] -= 1

        if pivot == -1:
            return ""

        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        for i in range(pivot):
            cnt[ord(target[i]) - ord('a')] -= 1

        x = ord(target[pivot]) - ord('a')

        for c in range(x + 1, 26):
            if cnt[c] > 0:
                cnt[c] -= 1
                greater = chr(c + ord('a'))
                break

        suffix = []

        for c in range(26):
            if cnt[c]:
                suffix.append(chr(c + ord('a')) * cnt[c])

        return target[:pivot] + greater + ''.join(suffix)