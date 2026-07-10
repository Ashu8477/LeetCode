class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        total = sorted(nums1+nums2)
        n=len(total)
        if n%2==0:
            i=n//2
            return (total[i]+total[i-1])/2

        else:
            i=n//2
            return total[i]


        