# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        arr=[]
        def solve(node):
            if node is None:
                return
            solve(node.left)
            arr.append(node.val)
            solve(node.right)
        solve(root)
        return arr[k-1]
        