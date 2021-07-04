var father=new Map()
var lowestCommonAncestor = function(root, p, q) {
    calfather(root,-1)
    red=new Set()
    red.add(root.val)
    while (father.get(p)!=-1){
        red.add(p.val)
        p=father.get(p)
    }
    while (!red.has(q.val)){
        q=father.get(q)
    }
    return q
};
var calfather=function(root,pre){
    father.set(root,pre)
    if (root.left!=null){
        calfather(root.left,root)
    }
    if (root.right!=null){
        calfather(root.right,root)
    }
}