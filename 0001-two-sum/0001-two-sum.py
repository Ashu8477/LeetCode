class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        n=len(nums)
        hashMap={}


        for i in range(n):
            value=target-nums[i]
            if value in hashMap:
                return hashMap[value],i
            hashMap[nums[i]]=i


        