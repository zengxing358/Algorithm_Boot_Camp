/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
 var isValidBST = function(root) {
    let arr=[];
    let inorder=(root)=>{
        if (root){
            inorder(root.left)
            arr.push(root.val)
            inorder(root.right)
        }
    };
    inorder(root)
    for (let i=0;i<arr.length-1;i++){
        if (arr[i+1]<=arr[i]){
            return false
        }
    }
    return true
};