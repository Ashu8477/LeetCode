class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n=len(nums)
        count={}
        for num in nums:
            count[num]=count.get(num,0)+1
        ans=0
        for num in count.values():
            ans+=num*(num-1)//2 
        return ans
        
        

        