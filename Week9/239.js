class Node{
    constructor(key,val){
        this.key=key
        this.val=val
        this.color="red"
        this.left=null
        this.right=null
    }
}
class RBTree{
    constructor(){
        this.root=null
    }
    insert(key,val){
        this.root=this.__insert(this.root,key,val)
        this.root.color="red"
    }
    isRed(node){
        if (node!=null){
            return node.color=="red"
        }
        return false
    }
    leftRotate(node){
        var y=node.right
        node.right=y.left
        y.left=node
        y.color=node.color
        node.color="red"
        return y
    }
    rightRotate(node){
        var y=node.left
        node.left=y.right
        y.right=node
        y.color=node.color
        node.color="red"
        return y
    }
    flipColors(node){
        node.color="red"
        node.left.color="black"
        node.right.color="black"
        return node
    }
    __insert(node,key,val){
        if(node==null){
            return new Node(key,val)
        }
        if (val<node.val){
            node.left=this.__insert(node.left,key,val)
        }else{
            node.right=this.__insert(node.right,key,val)
        }
        if (this.isRed(node.right) && (!this.isRed(node.left))){
            node=this.leftRotate(node)
        }
        if (this.isRed(node.left) && (this.isRed(node.left.left))){
            node=this.rightRotate(node)
        }
        if (this.isRed(node.right) && this.isRed(node.left)){
            node=this.flipColors(node)
        }
        return node
    }
    findMax(){
        var node=this.maxnum(this.root)
        return [node.key,node.val]
    }
    maxnum(node){
        if(node.right==null){
            return node
        }
        return this.maxnum(node.right)
    }
    extractMax(){
        this.root=this.removeMax(this.root)
    }
    removeMax(node){
        if(node.right==null){
            var rightNode=node.left;
            node.left=null;
            return rightNode;
        }
        node.right=this.removeMax(node.right);
        return node;
    }
}

var maxSlidingWindow = function(nums, k) {
    var tree=new RBTree()
    var res=[]
    var arr
    for(let i=0;i<nums.length;i++){
        tree.insert(i,nums[i])
        if(i>=k-1){
            while(true){
                arr=tree.findMax()
                if(i-arr[0]>=k){
                    tree.extractMax()
                }else{
                    break;
                }
            }
            res.push(arr[1])
        }
    }
    return res
};