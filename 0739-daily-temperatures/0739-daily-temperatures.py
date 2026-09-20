class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n=len(temperatures)
        ans=[0]*n
        stack=[]

        for i,temp in enumerate(temperatures):

            while stack and temperatures[stack[-1]]<temp:
                ans[stack.pop()]=i-stack[-1]


            stack.append(i)
        return ans


        