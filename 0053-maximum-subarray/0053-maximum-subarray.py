class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=nums[0]
        sum=nums[0]
        n=len(nums)
        for i in range(1,n):
            sum=max(nums[i],sum+nums[i])
            maxi=max(sum,maxi)
        return maxi
        