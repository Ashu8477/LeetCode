# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:

        def solve(total,node):
            if node is None:
                return False

            total+=node.val

            if node.left is None and node.right is None:
                return targetSum==total
            
            return solve(total,node.left) or solve(total,node.right)
        return solve(0,root)
        