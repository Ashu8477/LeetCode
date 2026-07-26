class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max1=max2=max3=float('-inf')
        mini1=mini2=float('inf')

        for num in nums:
            if num>max3:
                max1=max2 
                max2=max3 
                max3=num 
            elif num>max2:
                max1=max2 
                max2=num 
            elif num>max1:
                max1=num
            if num<mini1:
                mini2=mini1
                mini1=num
            elif num<mini2:
                mini2=num
        return max(max1 * max2 * max3, mini1 * mini2 * max3)
            
        