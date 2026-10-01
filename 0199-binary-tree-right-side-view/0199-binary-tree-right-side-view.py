# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        ans=[]
        def solve(node,level):
            if node is None:
                return
            if len(ans)==level:
                ans.append(node.val)
            solve(node.right,level+1)
            solve(node.left,level+1)
        solve(root,0)
        return ans