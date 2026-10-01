# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        check=True

        def solve(node):
            nonlocal check
            if node is None:
                return 0

            l=solve(node.left)
            r=solve(node.right)
            if abs(l-r) > 1:
                check = False

            return 1+max(l,r)
        solve(root)
        return check
    

        