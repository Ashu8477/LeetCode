class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n=len(nums)
        digit_count=[0]*101
        for num in nums:
            digit_count[num]+=1
        ans=0
        for num in digit_count:
            ans+=num*(num-1)//2 
        return ans
        
        

        