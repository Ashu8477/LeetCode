class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left=max(nums)
        right=sum(nums)

        while left<=right:
            mid=(left+right)//2

            sub_array=1
            curr_sum=0
            for num in nums:
                if curr_sum+num>mid:
                    sub_array+=1
                    curr_sum=0
                curr_sum+=num
            if sub_array<=k:
                right=mid-1
            else:
                left=mid+1
        return left
        