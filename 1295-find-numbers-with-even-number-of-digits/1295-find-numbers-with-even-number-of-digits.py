class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=1
        number=0
        even_number=0

        for num in nums:
            number=num//10
            while number>0:
                number//=10
                count+=1
            if count%2==0:
                even_number+=1
            count=1
        return even_number
            
        