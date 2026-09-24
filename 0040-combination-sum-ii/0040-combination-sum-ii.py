class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:

        ans=[]
        candidates.sort()

        def solve(path,start,total):
            if total==target:
                ans.append(path[:])
                return
            if total>target:
                return

            for i in range(start,len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                path.append(candidates[i])
                solve(path,i+1,total+candidates[i])
                path.pop()
            
        solve([],0,0)
        return ans
            
        