class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        n=len(nums)
        def solve(path,rem):
            ans.append(path[:])

            for i in range(len(rem)):
                if len(path)==len(nums):
                    return
                solve(path + [rem[i]],rem[i+1:])
        solve([],nums)
        return ans
        