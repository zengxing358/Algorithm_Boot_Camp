# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root:
            def dfs(root):
                nonlocal s
                if root.right:
                    dfs(root.right)
                s+=root.val
                root.val=s
                if root.left:
                    dfs(root.left)
            s=0
            dfs(root)
            return root

