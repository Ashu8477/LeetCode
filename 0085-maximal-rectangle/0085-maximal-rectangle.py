class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        col=len(matrix[0])
        ans=0
        heights=[0]*col
        max_area=0
        for row in matrix:
            for i in range(col):
                if row[i]=='1':
                    heights[i]+=1
                else:
                    heights[i]=0
            heights.append(0)
            stack=[]
            for i,h in enumerate(heights):
                while stack and heights[stack[-1]]>h:
                    height=heights[stack.pop()]
                    width=i if not stack else i-stack[-1]-1
                    max_area=max(max_area,height*width)
                stack.append(i)
        return max_area


        