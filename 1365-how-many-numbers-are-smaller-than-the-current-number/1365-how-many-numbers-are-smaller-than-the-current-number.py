class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n=len(nums)
        smaller=[]
        count=0
        for num in nums:
            for i in range(n):
                if nums[i]<num:
                    count+=1
            smaller.append(count)
            count=0
        return smaller
