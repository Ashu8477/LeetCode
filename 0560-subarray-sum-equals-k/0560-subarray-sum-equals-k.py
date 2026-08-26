class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        curr=0
        freq={0:1}

        for num in nums:
            curr+=num
            if curr-k in freq:
                count+=freq[curr-k]
            freq[curr]=freq.get(curr,0)+1
        return count
