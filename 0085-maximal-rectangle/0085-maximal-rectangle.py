class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        maxi=0
        n=len(matrix[0])
        stack=[0]*n
        for num in matrix: 
            for i in range(n):
                if num[i]=='1':
                    stack[i]+=1
                else:
                    stack[i]=0
            stack2=[]
            height=stack+[0]
            for i,row in enumerate(height):
                while stack2 and height[stack2[-1]]>row:
                    idx=stack2.pop() 
                    width=i if not stack2 else i-stack2[-1]-1
                    maxi=max(maxi,height[idx]*width)
                stack2.append(i)
            
        return maxi


        