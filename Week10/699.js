var fallingSquares = function(positions) {
    var dic=new Set()
    for ([left,length] of positions){
        right=left+length-1
        dic.add(left)
        dic.add(right)
    }
    var pos=Array.from(dic)
    pos.sort((a,b)=>{return a-b})
    var index=1
    var graph={}
    for (let p of pos){
        graph[p]=index
        index+=1
    }
    var res=[]
    var tree=new Array(index<<2).fill(0)
    var lazy=new Array(index<<2).fill(0)
    var push_down=function(idx){
        if (lazy[idx]>0){
            lazy[idx<<1]=lazy[idx]
            lazy[idx<<1|1]=lazy[idx]
            tree[idx<<1]=lazy[idx]
            tree[idx<<1|1]=lazy[idx]
            lazy[idx]=0
        }
    }
    var query=function(Left,Right,l,r,idx){
        if (Left<=l && Right>=r){
            return tree[idx]
        }
        push_down(idx)
        var mid=(l+r)>>1
        var res=0
        if (Left<=mid){
            res=Math.max(res,query(Left,Right,l,mid,idx<<1))
        }
        if (Right>mid){
            res=Math.max(res,query(Left,Right,mid+1,r,idx<<1|1))
        }
        return res
    }
    var push_up=function(idx){
        tree[idx]=Math.max(tree[idx<<1],tree[idx<<1|1])
    }
    var update=function(Left,Right,l,r,idx,val){
        if (Left<=l && Right>=r){
            tree[idx]=val
            lazy[idx]=val
            return
        }
        push_down(idx)
        var mid=(l+r)>>1
        if (Left<=mid){
            update(Left,Right,l,mid,idx<<1,val)
        }
        if (Right>mid){
            update(Left,Right,mid+1,r,idx<<1|1,val)
        }
        push_up(idx)
    }

    for ([left,length] of positions){
        var L=graph[String(left)]
        var r=left+length-1
        var R=graph[String(r)]
        var H=query(L,R,1,index,1)+length
        update(L,R,1,index,1,H)
        res.push(query(1,index,1,index,1))
    }
    return res
};