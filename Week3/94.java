class Solution {
    private List<Integer> ans=new ArrayList<>();
    public List<Integer> inorderTraversal(TreeNode root) {
        inorderTrave(root);
        return ans;
    }
    private void inorderTrave(TreeNode root){
        if (root!=null){
            if (root.left!=null){
                inorderTrave(root.left);
            }
            ans.add(root.val);
            if (root.right!=null){
                inorderTrave(root.right);
            }
        }
    }
}