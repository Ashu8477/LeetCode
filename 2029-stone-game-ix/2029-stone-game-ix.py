class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt = [0, 0, 0]

        for stone in stones:
            cnt[stone % 3] += 1

        cnt0, cnt1, cnt2 = cnt

        if cnt0 % 2 == 0:
            return cnt1 > 0 and cnt2 > 0

        return abs(cnt1 - cnt2) > 2