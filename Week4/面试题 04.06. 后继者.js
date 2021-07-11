var inorderSuccessor = function(root, p) {
    var res=null
    var Successor=function(root,node){
        if (root!=null && node!=null){
            if(root.val>node.val){
                if (res==null){
                    res=root
                }else if(res.val>root.val){
                    res=root
                }
                Successor(root.left,node)
            }else if (root.val==node.val){
                if (root.right!=null){
                    cur=root.right
                    while(cur.left!=null){
                        cur=cur.left
                    }
                    res=cur
                }
            }else{
                Successor(root.right,node)
            }
        }
    }
    Successor(root,p)
    return res
};