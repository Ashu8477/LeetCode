class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:

        mp={}
        stack=[]

        for num in nums2:
            while stack and stack[-1]<num:
                mp[stack.pop()]=num

            stack.append(num)
        
        return [mp.get(num,-1) for num in nums1]
        