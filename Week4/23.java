import java.util.Collections;
 class MinHeap{
     List<ListNode> data;
     int size;
        public MinHeap(){
            size=0;
            data=new ArrayList<ListNode>();
        }
        public boolean isempty(){
            return size==0;
        }
        private void swap(int i,int j){
            Collections.swap(data, i, j);
        }
        private void up(int index){
            if(index>0){
                int parent=(index-1)/2;
                if(data.get(index).val<data.get(parent).val){
                    swap(index,parent);
                    up(parent);
                }
            }
        }
        private void down(int index){
            if(size!=0){
                int left=index*2+1;
                int right=index*2+2;
                int successor=index;
                if(right<size && data.get(right).val<data.get(successor).val){
                    successor=right;
                }
                if(left<size && data.get(left).val<data.get(successor).val){
                    successor=left;
                }
                if(successor!=index){
                    swap(successor, index);
                    down(successor);
                }
            }
        }
        public void add(ListNode node){
            data.add(node);
            up(size);
            size+=1;
        }
        public ListNode pop(){
            size-=1;
            ListNode res=data.get(0);
            swap(0, size);
            data.remove(size);
            down(0);
            return res;
        }
    }
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        MinHeap heap=new MinHeap();
        ListNode res=new ListNode();
        ListNode cur=res;
        for(ListNode l:lists){
            if(l!=null){
                heap.add(l);
            }
        }
        while(!heap.isempty()){
            ListNode m=heap.pop();
            cur.next=m;
            if(m.next!=null){
                heap.add(m.next);
            }
            cur=cur.next;
        }
        return res.next;
    }
}