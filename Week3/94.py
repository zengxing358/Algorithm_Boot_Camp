'''
https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
非递归解法
'''
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack=[]
        res=[]
        cur=root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur=cur.left
            temp=stack.pop()
            res.append(temp.val)
            cur=temp.right
        return res