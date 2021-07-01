"""
https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root:
            res=[]
            queue=[root]
            while queue:
                temp=[]
                r=[]
                for item in queue:
                    r.append(item.val)
                    if item.children:
                        temp.extend(item.children)
                res.append(r)
                queue=temp
            return res
        return 