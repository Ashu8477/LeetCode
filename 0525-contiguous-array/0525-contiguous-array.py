class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n=len(nums)
        prefix=0
        hash={0:-1}
        ans=0
        for i in range(n):
            if nums[i]==0:
                prefix-=1
            else:
                prefix+=1
            if prefix in hash:
                ans = max(ans, i - hash[prefix])
            else:
                hash[prefix]=i
        return ans
        