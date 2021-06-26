/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
 var maxDepth = function(root) {
    let res=0;
    const dfs=(n,l)=>{
        if (!n){ return;}
        if (!n.left && !n.right){res=Math.max(res,l);}
        dfs(n.left,l+1);
        dfs(n.right,l+1);
    };
    dfs(root,1);
    return res;
};