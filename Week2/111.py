# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue=[[root]]
        count=0
        while queue:
            node=queue.pop()
            count+=1
            temp=[]
            for n in node:
                if not n.left and not n.right:
                    return count
                if n.left:
                    temp.append(n.left)
                if n.right:
                    temp.append(n.right)
            queue.append(temp)
                