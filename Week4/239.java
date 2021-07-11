import java.util.*;
class Solution {
public class MaxHeap{
    class Node{
        public int key;
        public int val;
        public Node(int key,int value){
            this.key=key;
            this.val=value;
        }
    }
    private ArrayList<Node> data;
    private int size;

    public MaxHeap(){
        data = new ArrayList<>();
        size=0;
    }

    public boolean isEmpty(){
        return size==0;
    }

    private int parent(int index){
        if(index == 0)
            throw new IllegalArgumentException("index-0 doesn't have parent.");
        return (index - 1) / 2;
    }

    private int leftChild(int index){
        return index * 2 + 1;
    }

    private int rightChild(int index){
        return index * 2 + 2;
    }

    // 向堆中添加元素
    public void add(int key,int value){
        Node node=new Node(key,value);
        data.add(node);
        siftUp(size);
        size++;
    }

    private void siftUp(int k){
        while(k > 0 && data.get(parent(k)).val<data.get(k).val){
            swap(k, parent(k));
            k = parent(k);
        }
    }

    public int[] findMax(){
        if(size == 0)
            throw new IllegalArgumentException("Can not findMax when heap is empty.");
        int []res=new int[]{data.get(0).val,data.get(0).key};
        return res;
    }

    private void swap(int p,int q){
        Node temp=data.get(p);
        data.set(p,data.get(q));
        data.set(q,temp);
    }

    public int[] extractMax(){
        int[] ret = findMax();
        size--;
        swap(0, size);
        data.remove(size);
        siftDown(0);
        return ret;
    }

    private void siftDown(int k){

        while(leftChild(k) < size){
            int j = leftChild(k); // 在此轮循环中,data[k]和data[j]交换位置

            if( j + 1 < size &&
                    data.get(j + 1).val>data.get(j).val )
                j ++;
            // data[j] 是 leftChild 和 rightChild 中的最小值

            if(data.get(k).val>data.get(j).val )
                break;

            swap(k, j);
            k = j;
        }
    }


}
    public int[] maxSlidingWindow(int[] nums, int k) {
        MaxHeap tree=new MaxHeap();
        int[] res=new int[nums.length-k+1];
        int []temp;
        for(int i=0;i<nums.length;i++){
                tree.add(i,nums[i]);
                if(i>=k-1){
                    while (true){
                        temp=tree.findMax();
                        if(i-temp[1]>=k){
                            tree.extractMax();    
                        }else{
                            break;
                        }
                    }
                    res[i-k+1]=temp[0];
                }
        }
        return res;
    }
}