class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i in range(len(nums)):
            value=target-nums[i]
            if value in dic:
                return dic[value],i
                
            else:
                dic[nums[i]]=i
       


        