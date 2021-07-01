public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if(root!=null){
            String res="";
            Queue<TreeNode> q=new LinkedList<>();
            if (root!=null) q.offer(root);
            while(!q.isEmpty()) {
                TreeNode node=q.poll();
                if (node!=null){
                    q.offer(node.left);
                    q.offer(node.right);
                    res+=Integer.toString(node.val)+",";
                }else{
                    res+="null,";
                }
            }
            res=res.substring(0,res.length()-1);
            return "["+res+"]";
        }
        return "";
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if(data.length()>2){
            String[] lst=data.substring(1, data.length()-1).split(",");
                TreeNode root=new TreeNode(Integer.valueOf(lst[0]));
                Integer cnt=1;
                Queue<TreeNode> q=new LinkedList<>();
                q.offer(root);
                while(cnt<lst.length){
                    TreeNode node=q.poll();
                    if (!lst[cnt].equals("null")){
                        node.left=new TreeNode(Integer.valueOf(lst[cnt]));
                        q.offer(node.left);
                    }
                    cnt+=1;
                    if (cnt<lst.length && !lst[cnt].equals("null")){
                        node.right=new TreeNode(Integer.valueOf(lst[cnt]));
                        q.offer(node.right);
                    }
                    cnt+=1;
                }
                return root;
        }
        return null;
    }
}