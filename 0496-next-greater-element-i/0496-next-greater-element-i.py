class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        mp={}
        for num in nums2:

            while stack and stack[-1]<num:
                mp[stack.pop()]=num

            stack.append(num)
        stack=[]
        for num in nums1:
            if num in mp:
                stack.append(mp[num])
            else:
                stack.append(-1)
        return stack
