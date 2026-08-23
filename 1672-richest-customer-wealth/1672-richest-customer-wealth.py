class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m=len(accounts)
        n=len(accounts[0])
        rich=0
        sum=0
        for i in range(m):
            for j in range(n):
                sum+=accounts[i][j]
            rich=max(rich,sum)
            sum=0
        return rich

        