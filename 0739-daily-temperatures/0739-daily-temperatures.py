class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n=len(temperatures)
        ans=[0]*n
        stack=[]

        for i,temp in enumerate(temperatures):

            while stack and temperatures[stack[-1]]<temp:
                ans[stack[-1]]=i-stack[-1]
                stack.pop()


            stack.append(i)
        return ans


        