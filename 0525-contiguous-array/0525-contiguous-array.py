class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hash={0:-1}
        count=0
        prefix=0
        n=len(nums)
        for i in range(n):
            if nums[i]==0:
                prefix-=1
            else:
                prefix+=1
            
            if prefix in hash:
                count=max(count,i-hash[prefix])
            else:
                hash[prefix]=i
        return count