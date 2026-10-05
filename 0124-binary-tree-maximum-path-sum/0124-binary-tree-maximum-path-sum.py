# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        maxi=float('-inf')
        
        def solve(node):
            nonlocal maxi
            if node is None:
                return 0
            
            l=max(0,solve(node.left))
            r=max(0,solve(node.right))
            maxi=max(maxi,(l+r+node.val))

            if l>r:
                return l + node.val
            else:
                return r + node.val
        solve(root)
        return maxi