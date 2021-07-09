class Solution {
    int rows,cols;
    int[] dirx={-1,0,0,1};
    int[] diry={0,-1,1,0};
    public int longestIncreasingPath(int[][] matrix) {
        rows=matrix.length;
        cols=matrix[0].length;
        int[][] dic=new int[rows][cols];
        int ans=0;
        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                ans=Math.max(ans, dfs(matrix,i,j,dic));
            }
        }
        return ans;
    }
    private int dfs(int[][] matrix,int x,int y,int[][] dic){
        if (dic[x][y]!=0){
            return dic[x][y];
        }
        for(int cnt=0;cnt<4;cnt++){
                int nx=x+dirx[cnt];
                int ny=y+diry[cnt];
                if(nx>=0 && nx<rows && ny>=0 && ny<cols && matrix[nx][ny]>matrix[x][y]){
                    dic[x][y]=Math.max(dic[x][y],dfs(matrix,nx,ny,dic)+1);
                }
        }
        if (dic[x][y]==0){
            dic[x][y]=1;
        }
        return dic[x][y];
    }
}