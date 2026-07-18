class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_product=1
        min_product=1
        max_product=nums[0]
        for num in nums:
            if num<0:
                curr_product,min_product=min_product,curr_product
            curr_product=max(num,curr_product*num)
            min_product=min(num,min_product*num)
            max_product=max(max_product,curr_product)
            
        return max_product
        