class Solution {
    public int[] findRedundantConnection(int[][] edges) {
        int n=edges.length;
        int[] parent=new int[n+1];
        for (int i=1;i<=n;i++){
            parent[i]=i;
        }
        for (int i=0;i<n;i++){
            boolean con=connect(parent,edges[i][0],edges[i][1]);
            if (!con){
                if(edges[i][0]>edges[i][1]){
                    return new int[]{edges[i][1],edges[i][0]};
                }
                return new int[]{edges[i][0],edges[i][1]};
            }
        }
        return new int[]{};
    }
    public boolean connect(int[] parent,int u,int v){
        int rootu=getparent(parent,u);
        int rootv=getparent(parent,v);
        if (rootu!=rootv){
            parent[rootv]=rootu;
            return true;
        }
        return false;
    }
    private int getparent(int[] parent,int node){
        if (node!=parent[node]){
            return getparent(parent,parent[node]);
        }
        return node;
    }
}