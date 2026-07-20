class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_sum=0
        curr_sum=0

        m=len(accounts)
        n=len(accounts[0])
        for i in range(m):
            for j in range(n):
                curr_sum+=accounts[i][j]
            max_sum=max(max_sum,curr_sum)
            curr_sum=0
        return max_sum
                

        