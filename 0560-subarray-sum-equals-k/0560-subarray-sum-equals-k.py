class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash={0:1}
        prefix_sum=0
        count=0
        for i in nums:
            prefix_sum+=i
            if prefix_sum-k in hash:
                count+=hash[prefix_sum-k]
            hash[prefix_sum]=hash.get(prefix_sum,0)+1
        return count
        