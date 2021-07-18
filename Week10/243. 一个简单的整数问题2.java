import java.util.HashMap;
import java.util.Scanner;

public class Main {

    static class SegmentTree{
        private class Node{
            private int Left;
            private int Right;
            public Node(int left,int right){
                Left=left;
                Right=right;
            }
            public long getLength(){
                return (long)(Right-Left+1);
            }
        }
        private int N;
        private long[] arr;
        private long[] lazy;
        HashMap<Integer,Node> dic;
        public SegmentTree(int n){
            N=n;
            int size=(int)(N*4);
            arr=new long[size];
            lazy=new long[size];
            dic=new HashMap<>();
        }
        public void build(long[] nums){
            build(nums,0,N-1,0);
        }
        private int getLeft(int index){
            return (index<<1)|1;
        }
        private int getRight(int index){
            return (index<<1)+2;
        }
        private void build(long[] nums,int left,int right,int index){
            Node node=new Node(left,right);
            dic.put(index,node);
            if(left==right){
                arr[index]=nums[left];
                return;
            }
            int mid=(left+right)>>1;
            build(nums,left,mid,getLeft(index));
            build(nums,mid+1,right,getRight(index));
            push_up(index);
        }
        private void push_up(int index){
            arr[index]=arr[getLeft(index)]+arr[getRight(index)];
        }
        public long query(int left,int right){
            return query(left,right,0,N-1,0);
        }
        private long query(int left,int right,int l,int r,int index){
            if ((left<=l) && (right>=r)){
                return arr[index];
            }
            if ((left>r) || (right<l)){
                return 0;
            }
            push_down(index);
            int mid=(l+r)>>1;
            return query(left,right,l,mid,getLeft(index))+query(left,right,mid+1,r,getRight(index));
        }
        private void push_down(int index){
            if (lazy[index]!=0){
                int left=getLeft(index);
                int right=getRight(index);
                lazy[left]+=lazy[index];
                lazy[right]+=lazy[index];
                arr[left]+=lazy[index]*dic.get(left).getLength();
                arr[right]+=lazy[index]*dic.get(right).getLength();
                lazy[index]=0;
            }
        }
        public void update(int left,int right,int val){
            update(left,right,0,N-1,0,(long)val);
        }
        private void update(int left,int right,int l,int r,int index,long val){
            if ((left<=l) && (right>=r)){
                arr[index]+=val*(r-l+1);
                lazy[index]+=val;
                return;
            }
            push_down(index);
            int mid=(l+r)>>1;
            if (left<=mid){
                update(left,right,l,mid,getLeft(index),val);
            }
            if (right>mid){
                update(left,right,mid+1,r,getRight(index),val);
            }
            push_up(index);
        }
    }


    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();

        long[] a = new long[n];
        for(int i = 0; i < n; i++){
            a[i] = (long)in.nextInt();
        }
        SegmentTree tree=new SegmentTree(n);
        tree.build(a);
        while(m -- > 0){
            String s = in.next();
            int x = in.nextInt();
            int y = in.nextInt();
            if(s.charAt(0) == 'Q') {
                System.out.println(tree.query(x - 1, y - 1));
            }else{
                tree.update(x-1, y-1, in.nextInt());
            }
        }
    }
}