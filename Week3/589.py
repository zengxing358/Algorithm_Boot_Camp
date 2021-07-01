"""
https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/
非递归解法
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root:
            res=[]
            queue=[root]
            while queue:
                item=queue.pop()
                res.append(item.val)
                if item.children:
                    queue.extend(item.children[::-1])
            return res
        return