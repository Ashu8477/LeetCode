class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
  
        mini_val=[0]*n
        mini_val[n-1]=nums[n-1]

        
        for j in range(n-2,-1,-1):
            mini_val[j]=min(mini_val[j+1],nums[j])

        maxi=float('-inf')

        for i in range(n):
            maxi=max(nums[i],maxi)
            
            if maxi-mini_val[i]<=k:
                return i
        return -1

        