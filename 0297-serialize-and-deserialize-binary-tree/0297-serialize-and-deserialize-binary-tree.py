# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        data=[]

        def solve(node):
            nonlocal data
            if node is None:
                data.append('N')
                return
            data.append(str(node.val))
            solve(node.left)
            solve(node.right)
        solve(root)
        return ",".join(data)

        #data=[1,2,N,N,3,4,N,N,5,N,N]

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        idx=0
        values = data.split(",")
        def solve(node):
            nonlocal idx
            if node[idx]=='N':
                idx+=1
                return None
            root=TreeNode(int(node[idx]))
            idx+=1
            root.left=solve(node)
            root.right=solve(node)
            return root
        return solve(values)

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))