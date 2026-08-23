class Solution:
    def findNumbers(self, nums: List[int]) -> int:

        even_digits=0

        for num in nums:

            if len(str(num))%2==0:
                even_digits+=1
        return even_digits
        