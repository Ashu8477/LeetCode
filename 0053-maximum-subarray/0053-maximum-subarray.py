class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=float(-inf)
        sum=nums[0]
        n=len(nums)
        if n==1:
            return nums[0]
        for i in range(1,n):
            if sum>maxi:
                 maxi=max(sum,maxi)
            sum+=nums[i]
            if nums[i]>sum:
                sum=nums[i]
            maxi=max(sum,maxi)
        return maxi
        