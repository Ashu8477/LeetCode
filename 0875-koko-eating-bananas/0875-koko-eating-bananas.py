class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left=1
        right=max(piles)

        while left<=right:

            k=(left+right)//2

            hours=0
            for banana in piles:
                hours+=(banana+(k-1))//k


            if hours<=h:
                right=k-1
            else:
                left=k+1
        return left