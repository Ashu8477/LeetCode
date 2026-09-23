class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        ans=[]

        def solve(path,rem):
            if not rem and path not in ans:
                ans.append(path)
                return
            elif path in ans:
                return
            for i in range(len(rem)):
                solve(path + [rem[i]],rem[:i]+rem[i+1:])
            
        solve([],nums)
        return ans
        