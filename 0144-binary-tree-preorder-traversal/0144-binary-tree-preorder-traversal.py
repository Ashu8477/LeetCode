# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        ans=[]

        def solve(node):

            if node is None:
                return
            
            ans.append(node.val)
            solve(node.left)
            solve(node.right)

        solve(root)
        return ans