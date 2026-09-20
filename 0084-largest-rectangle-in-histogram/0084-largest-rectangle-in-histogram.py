class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack=[]
        heights.append(0)
        maxi=0

        for i,height in enumerate(heights):
            while stack and heights[stack[-1]]>height:
                idx=stack.pop()
                width=i if not stack else i-stack[-1]-1
                maxi=max(maxi,heights[idx]*width)
            stack.append(i)
        return maxi
        