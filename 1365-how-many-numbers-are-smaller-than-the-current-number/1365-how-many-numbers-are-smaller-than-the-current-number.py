class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        n=[0]*101

        for num in nums:
            n[num]+=1
        for i in range(1,101):
            n[i]+=n[i-1]
        ans=[]
        for num in nums:
            if num==0:
                ans.append(0)
            else:
                ans.append(n[num-1])
        return ans

        