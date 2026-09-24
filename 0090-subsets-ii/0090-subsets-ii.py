class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        nums.sort()
        def solve(path,start):
            ans.append(path[:])

            for i in range(start,len(nums)):

                if i>start and nums[i]==nums[i-1]:
                    continue
                
                path.append(nums[i])
                solve(path,i+1)
                path.pop()


        solve([],0)
        return ans
        