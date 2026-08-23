class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        n=len(nums)
        count=0
        even_digit=0
        for num in nums:
            while num>0:
                last_digit=num%10
                count+=1
                num=num//10
            if count%2==0:
                even_digit+=1
            count=0

        return even_digit