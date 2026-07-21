class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq=[0]*101
        for num in nums:
            freq[num]+=1
        for i in range(101):  
            freq[i]=freq[i]*(freq[i]-1)//2

        count=0
        for x in freq:
            count += x
        return count










        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]==nums[j] and i!=j :
                    count+=1
        return count//2

        