# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        res=[]
        def order(root):
            if root:
                order(root.left)
                res.append(root)
                order(root.right)
        order(root)
        index=res.index(p)
        if index==len(res)-1:
            return
        else:
            return res[index+1]