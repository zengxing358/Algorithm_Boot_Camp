import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    static class Node{
        public int val;
        public int day;
        public Node(int val,int day){
            this.val=val;
            this.day=day;
        }
    }
    static class Heap{
        public Node[] heap;
        public int size;
        public Heap(int n){
            heap=new Node[n];
            size=0;
        }
        public boolean isEmpty(){
            return size==0;
        }
        public void add(Node node){
            heap[size]=node;
            up(size);
            size+=1;
        }
        public void up(int idx){
            if(idx>0){
                int parent=(idx-1)>>1;
                if(heap[parent].val<heap[idx].val){
                    swap(parent,idx);
                    up(parent);
                }
            }
        }
        public void swap(int p,int q){
            Node temp=heap[p];
            heap[p]=heap[q];
            heap[q]=temp;
        }
        public Node pop(){
            Node res=heap[0];
            size-=1;
            swap(0,size);
            down(0);
            heap[size]=null;
            return res;
        }
        public void down(int idx){
            int left=((idx<<1)+1);
            int right=((idx<<1)+2);
            int cur=idx;
            if(left<size && heap[cur].val<heap[left].val){
                cur=left;
            }
            if(right<size && heap[cur].val<heap[right].val){
                cur=right;
            }
            if(cur!=idx){
                swap(idx,cur);
                down(cur);
            }
        }
    }

    static class UnionFind{
        public int[] parent;
        public int size;
        public UnionFind(int size){
            parent=new int[size];
            for(int i=0;i<size;i++){
                parent[i]=-10;
            }
            this.size=0;
        }
        public int getSize(){
            return size;
        }
        public int find(int day){
            if (day>0){
                if (parent[day]==-10){
                    size+=1;
                    parent[day]=day-1;
                    return parent[day];
                }else if(parent[day]>0){
                    int k=find(parent[day]);
                    if (k>=0){
                        parent[day]=k;
                        return parent[day];
                    }else{
                        return k;
                    }
                }
            }
            return -1;
        }
    }

    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        while (sc.hasNext()){
            int n=sc.nextInt();
            Heap heap=new Heap(n);
            int maxday=0;
            for(int i=0;i<n;i++){
                int v=sc.nextInt();
                int d=sc.nextInt();
                maxday=Math.max(maxday,d);
                heap.add(new Node(v,d));
            }
            UnionFind union=new UnionFind(maxday+1);
            int ans=0;
            
            while(!heap.isEmpty() && union.getSize()<maxday){
                Node cur=heap.pop();
                int temp=union.find(cur.day);
                if (temp>=0){
                    ans+=cur.val;
                }
            }
            System.out.println(ans);
        }
    }
}