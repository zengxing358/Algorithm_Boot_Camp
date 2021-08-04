import java.util.*;

public class Main {
    public static Long[] arr;
    public static int W;
    public static int N;
    public static int k;
    public static HashSet weight;
    public static long ans;
    public static Long[] w;
    public static int cnt;
    public static void dfs1(int idx,long s){
        if (idx==k){
            weight.add(s);
            return;
        }
        dfs1(idx+1,s);
        if (s+arr[idx]<=W){
            dfs1(idx+1,s+arr[idx]);
        }
    }
    public static void dfs2(int idx,long s){
        if (idx==N){
            int left=-1;
            int right=cnt-1;
            while(left<right){
                int mid=((right+left+1)>>1);
                if(w[mid]<=W-s){
                    left=mid;
                }else{
                    right=mid-1;
                }
            }
            ans=Math.max(ans,w[left]+s);
            return ;
        }
        dfs2(idx+1,s);
        if (s+arr[idx]<=W){
            dfs2(idx+1,arr[idx]+s);
        }
    }
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        W=sc.nextInt();
        N=sc.nextInt();
        arr=new Long[N];
        for(int i=0;i<N;i++){
            arr[i]=sc.nextLong();
        }
        Arrays.sort(arr, Collections.reverseOrder());
        k=(N>>1)+1;
        weight=new HashSet();
        dfs1(0,0);
        w= (Long[])weight.toArray(new Long[weight.size()]);
        Arrays.sort(w);
        cnt=w.length;
        ans=0;
        dfs2(k,0);
        System.out.println(ans);
    }
}