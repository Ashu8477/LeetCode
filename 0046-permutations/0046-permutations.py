class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:

        ans=[]
        def solve(path,rem):
            if not rem:
                ans.append(path)
                return
            for i in range(len(rem)):
                solve(path + [rem[i]],rem[:i]+rem[i+1:])
        solve([],nums)
        return ans
        