class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        n=len(nums)
        n1=[]
        n2=[]
        n3=[]

        for num in nums[:n//2]:
            n1.append(num)
        for num in nums[n//2:]:
            n2.append(num)
       

        for i in range(n//2):
            n3.append(n1[i])
            n3.append(n2[i])
        return n3
        