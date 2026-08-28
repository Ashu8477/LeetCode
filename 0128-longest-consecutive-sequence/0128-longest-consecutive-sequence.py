class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        s = set(nums)

        if len(nums) == 0:
            return 0

        count = 1
        maxi = 1

        for num in nums:
            if num - 1 in s:
                count += 1
                maxi = max(count, maxi)
            else:
                count = 1

        return maxi