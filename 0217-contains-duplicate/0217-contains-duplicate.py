class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        count={}
          
        for num in nums:
            count[num]=count.get(num,0)+1
        
        for key,num in count.items():
            if num>1:
                return True
        return False
            