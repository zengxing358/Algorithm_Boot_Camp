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
        if (left<this.Size()){
            let minv=this.heap[left].val;
            let next=left;
            const right=index*2+2;
            if (right<this.Size() && this.heap[right].val<minv){
                minv=this.heap[right].val;
                next=right;};
            if (this.heap[index].val>minv){
                this.Swap(index,next);
                this.Down(next);};
        };
    }
    Up(index){
        if (index>0){
            const parent=(index-1)>>1;
            if (this.heap[index].val<this.heap[parent].val){
                this.Swap(index,parent);
                this.Up(parent);
            }
        }
    }
    Pop(){
        if (this.Size()===1){ return this.heap.shift()};
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
    Insert(value){
        this.heap.push(value);
        this.Up(this.Size()-1);
    }
};
var mergeKLists = function(lists) {
    const h=new MinHeap();
    lists.forEach( item =>{
        if(item) {
            h.Insert(item)};}
    );
    const node=new ListNode(0);
    let res=node;
    while (h.Size()){
        let n = h.Pop();
        res.next=n;
        console.log(n);
        if (n.next!=null) h.Insert(n.next);
        res=res.next;
    }
    return node.next
};