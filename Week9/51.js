var solveNQueens = function(n) {
    var res=[]
    var s=new Array(n).join(".")
    var slove=function(row,temp,cols,xs,ys){
        if (row==n){
            res.push(temp)
        }else{
            for(let j=0;j<n;j++){
                if ((!cols.has(j)) && (!xs.has(row-j)) && (!ys.has(row+j))){
                    var cur=`${s.slice(0,j)}Q${s.slice(j)}`
                    temp.push(cur)
                    cols.add(j)
                    xs.add(row-j)
                    ys.add(row+j)
                    slove(row+1,Array.from(temp),cols,xs,ys)
                    temp.pop()
                    cols.delete(j)
                    xs.delete(row-j)
                    ys.delete(row+j)
                }
            }
        }
    }
    slove(0,[],new Set(),new Set(),new Set())
    return res
};