class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.dp={}
        return self.__maxPathSum(root)
    def __maxPathSum(self,root):
        if root:
            self.dp[root]=[-float("inf"),root.val,root.val,root.val]
            left=0
            right=0
            if root.left:
                self.dp[root][0]=max(self.dp[root][0],self.__maxPathSum(root.left))
                left=max(self.dp[root.left][1],self.dp[root.left][2])
            if root.right:
                self.dp[root][0]=max(self.dp[root][0],self.__maxPathSum(root.right))
                right=max(self.dp[root.right][1],self.dp[root.right][2])
            self.dp[root][3]+=(left+right)
            if left>right:
                self.dp[root][2]+=left
            else:
                self.dp[root][2]+=right
            if root.left or root.right:
                return max(self.dp[root])
            return root.val
        return 0