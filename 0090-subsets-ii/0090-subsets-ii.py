class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        nums.sort()
        def solve(path,used,start):
            ans.append(path[:])

            for i in range(start,len(nums)):
                if used[i]:
                    continue
                if i>0 and nums[i]==nums[i-1] and not used[i-1]:
                    continue
                
                used[i]=True
                path.append(nums[i])
                solve(path,used,i+1)
                used[i]=False
                path.pop()


        solve([],[False]*len(nums),0)
        return ans
        