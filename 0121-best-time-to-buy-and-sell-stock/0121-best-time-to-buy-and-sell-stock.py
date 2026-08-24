class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        mini=float('inf')
        profit=0

        for num in prices:
            mini=min(num,mini)
            profit=max(profit,num-mini)
        return profit
            