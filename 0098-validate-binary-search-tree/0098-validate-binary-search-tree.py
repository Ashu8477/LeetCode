# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:

        def solve(node,low,high):
            if not node:
                return True
            if node.val<=low or node.val>=high:
                return False
            return solve(node.left,low,node.val) and solve(node.right,node.val,high)
        return solve(root,float('-inf'),float('inf'))
        