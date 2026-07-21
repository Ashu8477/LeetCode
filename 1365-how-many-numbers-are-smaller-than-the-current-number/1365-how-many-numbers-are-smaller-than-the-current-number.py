class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count=0
        new=[]
        i,j=0,0
        n = len(nums)

        for i in range(n):
            for j in range(n):
                if nums[i]>nums[j]:
                    count+=1
            new.append(count)
            count=0
        return new

        

        