var longestIncreasingPath = function(matrix) {
    var graph={}
    var degree={}
    var row=matrix.length
    var col=matrix[0].length
    var num=row*col
    var getcode=function(x,y){
        return x*col+y
    }
    var addedge=function(idx,nidx,i,j,x,y){
        if(matrix[i][j]>matrix[i+x][j+y]){
            if (!(nidx in graph)) {
            graph[nidx]=[]
            }
            graph[nidx].push(idx)
            if (!(idx in degree)){
                degree[idx]=0
            }
            degree[idx]+=1
        }else{
            graph[idx].push(nidx)
            if (!(nidx in degree)){
                degree[nidx]=0
            }
            degree[nidx]+=1
        }
    }
    for(let i=0;i<row;i++){
        for(let j=0;j<col;j++){
            var idx=getcode(i,j)
            if (!(idx in graph)) {
                    graph[idx]=[]
                }
            if(i+1<row && matrix[i][j]!=matrix[i+1][j]){
                var nidx=getcode(i+1,j)
                addedge(idx,nidx,i,j,1,0)
            }
            if(j+1<col && matrix[i][j]!=matrix[i][j+1]){
                var nidx=getcode(i,j+1)
                addedge(idx,nidx,i,j,0,1)
            }
        }
    }
    var hold=new Set()
    var dic={}
    for(let i=0;i<num;i++){
        if (!(i in degree)){
            hold.add(i)
        }
        dic[i]=1
    }
    var res=0
    var dfs=function(node){
        if (dic[node]!=1){
            return dic[node]
        }
        if (node in graph){
            for (let nxt of graph[node]){
                dic[node]=Math.max(dfs(nxt)+1,dic[node])
            }
        }
        res=Math.max(res,dic[node])
        return dic[node]
    }
    for (let node of hold){
        dfs(node)
    }
    return res
};