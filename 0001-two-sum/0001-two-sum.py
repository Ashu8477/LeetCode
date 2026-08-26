class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count={}
       


        for i in range(len(nums)):
            value=target-nums[i]
            if value not in count:
                count[nums[i]]=i
            else:
                return i,count[value]

        