class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxi = 0
        for num in s:
            if num - 1 not in s:
                count = 1
                while num + count in s:
                    count+=1
                maxi = max(count, maxi)
        return maxi