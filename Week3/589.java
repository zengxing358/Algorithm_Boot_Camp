class Solution {
    private List<Integer> ans=new ArrayList<>();
    public List<Integer> preorder(Node root) {
        PreOrder(root);
        return ans;
    }
    private void PreOrder(Node root){
        if (root!=null){
            ans.add(root.val);
            for(Node child:root.children){
                PreOrder(child);
            }
        }
    }
}