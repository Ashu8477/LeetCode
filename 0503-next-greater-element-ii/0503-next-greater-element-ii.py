class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n=len(nums)
        stack=[]
        ans=[-1]*n
        for i in range(n*2-1,-1,-1):

            num=nums[i%n]

            while stack and stack[-1]<=num:
                stack.pop()
            
            if i<n:
                if stack:
                    ans[i]=stack[-1]


            stack.append(num)
        return ans