class Solution:
    def sortColors(self, nums: List[int]) -> None:

        n=len(nums)
        i=0
        m=0
        j=n-1
        while m<=j:
            if nums[m]==2:
                nums[m],nums[j]=nums[j],nums[m]
                j-=1
            elif nums[m]==0:
                nums[i],nums[m]=nums[m],nums[i]
                i+=1
                m+=1
            else:
                m+=1
