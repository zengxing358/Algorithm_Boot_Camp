from functools import lru_cache
class Solution:
    @lru_cache(None)
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self._rob(root,True),self._rob(root,False))
    @lru_cache(None)
    def _rob(self,root,rob):
        if rob:
            value=root.val
            if root.left:
                value+=self._rob(root.left,False)
            if root.right:
                value+=self._rob(root.right,False)
            return value
        else:
            value=0
            if root.left:
                value+=self.rob(root.left)
            if root.right:
                value+=self.rob(root.right)
            return value