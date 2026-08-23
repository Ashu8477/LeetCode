class Solution:
    def findNumbers(self, nums: List[int]) -> int:

        even_digits=0

        for num in nums:

            if 10<=num<=99 or 1000<=num<=9999 or num==100000:
                even_digits+=1
        return even_digits