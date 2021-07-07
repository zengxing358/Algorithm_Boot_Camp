class MinHeap{
    constructor(){
        this.heap=[];
    }
    Size(){
        return this.heap.length
    }
    Swap(a,b){
        let temp=this.heap[a];
        this.heap[a]=this.heap[b];
        this.heap[b]=temp;
    }
    Down(index){
        const left=index*2+1;
        if (left<=this.Size()){
            let minv=this.heap[left];
            let next=left;
            const right=index*2+2;
            if (right<=this.Size() && this.heap[right]<minv){
                minv=this.heap[right];
                next=right;};
            if (this.heap[index]>minv){
                this.Swap(index,next);
                this.Down(next);};
        };
    }
    Up(index){
        if (index>0){
            const parent=(index-1)>>1;
            if (this.heap[index]<this.heap[parent]){
                this.Swap(index,parent);
                this.Up(parent);
            }
        }
    }
    Pop(){
        let result=this.heap[0];
        this.heap[0]=this.heap.pop();
        this.Down(0);
        return result;
    }
    Recont(lst){
        this.heap=lst;
        for (let i=((this.Size()-1)>>1);i>=0;i--){
            this.Down(i);
        }
    }
};
var findKthLargest = function(nums, k) {
    const heap=new MinHeap();
    heap.Recont(nums)
    while (heap.Size()>k){
        heap.Pop()
    }
    return heap.Pop()
};