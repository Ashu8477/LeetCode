class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        n=[0]*101

        for num in nums:
            n[num]+=1
        for i in range(1,101):
            n[i]+=n[i-1]
        return [n[num-1] if num>0 else 0 for num in nums]

        