class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        ans=[]

        def solve(path,start):
            if sum(path)==target:
                ans.append(path[:])
                return
            if sum(path)>target:
                return
            
            for i in range(start,len(candidates)):
                path.append(candidates[i])
                solve(path,i)
                path.pop()
        solve([],0)
        return ans


        