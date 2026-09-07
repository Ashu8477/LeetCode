class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        left=max(weights)
        right=sum(weights)

        while left<=right:

            k=(left+right)//2

            day=1
            summ=0

            for weight in weights:

                summ+=weight
                if summ>k:
                    summ=weight
                    day+=1

            if day<=days:
                right=k-1
            else:
                left=k+1
        return left
        