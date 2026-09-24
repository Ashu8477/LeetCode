class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        ans=[]

        def solve(path,start,total):
            if total==target:
                ans.append(path[:])
                return
            if total>target:
                return
            
            for i in range(start,len(candidates)):
                path.append(candidates[i])
                solve(path,i,total+candidates[i])
                path.pop()
        solve([],0,0)
        return ans


        