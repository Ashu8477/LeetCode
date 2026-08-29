class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        n=len(nums)
        
        maxi=0
        for num in nums:
            count=0
            if num-1 not in nums:
                count=1
                while num + count in nums:
                    count+=1 
            maxi=max(maxi,count)
            count=0
        return maxi
            

        