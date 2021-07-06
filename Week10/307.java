class NumArray {
    private class SegmentTree<E> {
    
        private  E[] data;
        private  E[] tree;
        private  Merger<E> merger;
        public SegmentTree(E[] arr,Merger<E> merger){
            this.merger=merger;
            data=(E[])new Object[arr.length];
            for(int i=0;i<arr.length;i++)
                data[i]=arr[i];
    
            tree=(E[])new Object[4*arr.length];
            buildSegmentTree(0,0,data.length-1);
    
        }
        private void buildSegmentTree(int treeIndex,int l,int r){
            if(l==r){
                tree[treeIndex]=data[l];
                return;
            }
            int leftTreeIndex=leftChild(treeIndex);
            int rightTreeIndex=rightChild(treeIndex);
            int mid=l+(r-l)/2;
            buildSegmentTree(leftTreeIndex,l,mid);
            buildSegmentTree(rightTreeIndex,mid+1,r);
            tree[treeIndex]=merger.merger(tree[leftTreeIndex],tree[rightTreeIndex]);
        }
    
        public int getSize(){
            return data.length;
        }
    
        public E get(int index){
            if(index<0 || index>=data.length)
                throw new IllegalArgumentException("Index is illegal.");
            return data[index];
        }
    
        private int leftChild(int index){
            return 2*index+1;
        }
        private int rightChild(int index){
            return 2*index+2;
        }
    
        public E query(int queryL,int queryR){
            if(queryL<0||queryR<0||queryL>=data.length||queryR>=data.length||queryL>queryR)
                throw new IllegalArgumentException("Index is illegal.");
            return query(0,0,data.length-1,queryL,queryR);
        }
    
        private E query(int treeIndex,int l,int r,int queryL,int queryR){
            if (l==queryL && r==queryR)
                return tree[treeIndex];
            int mid=l+(r-l)/2;
            int leftTreeIndex=leftChild(treeIndex);
            int rightTreeIndex=rightChild(treeIndex);
            if (queryR<=mid) {
                return query(leftTreeIndex, l, mid, queryL, queryR);
            }else if(queryL>mid){
                return query(rightTreeIndex,mid+1,r,queryL,queryR);
            }else {
                E left = query(leftTreeIndex, l, mid, queryL,mid);
                E right=query(rightTreeIndex,mid+1,r,mid+1,queryR);
                return merger.merger(left,right);
            }
        }
    
        public void set(int index,E e){
            if (index<0 || index>=data.length)
                throw new IllegalArgumentException("Index is illegal");
            data[index]=e;
            set(0,0,data.length-1,index,e);
        }
    
        private void set(int treeIndex,int l,int r,int index ,E e){
            if (l==r){
                tree[treeIndex]=e;
                return;
            }
            int mid=l+(r-l)/2;
            int leftIndex=leftChild(treeIndex);
            int rightIndex=rightChild(treeIndex);
            if (index<=mid){
                set(leftIndex,l,mid,index,e);
            }else{
                set(rightIndex,mid+1,r,index,e);
            }
    
            tree[treeIndex]=merger.merger(tree[leftIndex],tree[rightIndex]);
        }
    }
    private interface Merger<E>{
        E merger(E a ,E b);
    }
    
        private SegmentTree<Integer> segmentTree;
        public NumArray(int[] nums) {
            if(nums.length>0){
                Integer[] data=new Integer[nums.length];
                for(int i=0;i<nums.length;i++){
                    data[i]=nums[i];
                }
                segmentTree =new SegmentTree<>(data,(a,b)->a+b);}
        }
        
        public void update(int i, int val) {
               if(segmentTree==null){
                throw new IllegalArgumentException("Segment Tree is null");
            }
            segmentTree.set(i,val);
        }
        
        public int sumRange(int i, int j) {
            if(segmentTree==null){
                throw new IllegalArgumentException("Segment Tree is null");
            }
            return segmentTree.query(i,j);
        }
    }
    
    /**
     * Your NumArray object will be instantiated and called as such:
     * NumArray obj = new NumArray(nums);
     * obj.update(i,val);
     * int param_2 = obj.sumRange(i,j);
     */