class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans=[]

        def solve(start,path):
            ans.append(path[:])

            for i in range(start,len(nums)):
                path.append(nums[i])
                solve(i+1,path)
                path.pop()
        
        solve(0,[])
        return ans
        